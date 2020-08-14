from room import Room
from player import Player
from world import World

import os
dirpath = os.path.dirname(os.path.abspath(__file__))
# map_file = dirpath + "/maps/main_maze.txt"

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = dirpath + "/maps/test_line.txt"
# map_file = dirpath + "/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = dirpath + "/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

traversal_path = []

# #Use a stack to keep track of the path
# s = Stack()
# #Set start to 0
# start = player.current_room.id
# #Set for visited
# visited = set()
# # Check if length of visited is less than length of graph
# while len(visited) < len(room_graph):
#    #Use another stack to keep track of posibble next moves
#    # ???
#    #Set the current room
#    this_room = s.pop()
#    #Add current room to visited
#    if this_room not in visited:
#        visited.add(this_room)
# print(visited)
   #Check for possible moves in current room
   #Loop through possible moves
      #Check if rooms have been visited or not
         #If not add to next moves stack
   #If next move push it to path
   # otherwise remove it from path and set the room traversal
   #Loop through rooms if the next room is the traversal room append it to traversal.



### CLOSEST ATTEMPT SO FAR ###
press_start = player.current_room.id
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversal_graph = {}
explored = {}
current_path = []

# print("ROOM LENGTH", len(room_graph))

def traverse(starting_point):
    # print("TRAVERSAL STATUS", traversal_graph, len(traversal_graph))
    # print("TRAVERSAL",len(traversal_graph))
    # print("EXPLORED", len(explored))
    # base case
    if len(explored) == len(room_graph):
        return
    
    s = Stack()
    s.push(starting_point)
    # print("path start")
    while s.size() > 0:
    # track previous room (start_room)
        # print("stack is running")
        # print(current_path)
        # player current room
        start_room = s.pop()
        # get all the possible exits
        exits = player.current_room.get_exits()
        if start_room is None:
            return
        if start_room not in traversal_graph:
            traversal_graph[start_room] = {}
            for pathway in exits:
                traversal_graph[start_room][pathway] = '?'
        # direction = random n e s w random
        # traverse to room player.travel(direction)
        # filter directions to only be random unexplored
        unexplored_exits = [way for way in traversal_graph[start_room] if traversal_graph[start_room][way] == '?']
        # print("unexplored after initialization", unexplored_exits)
        # if there is an exit to explore
        if len(unexplored_exits) > 0:
            # print("unexplored in stack", unexplored_exits)
            direction = random.choice(unexplored_exits)
            # travel
            player.travel(direction)
            traversal_path.append(direction)
            current_path.append(direction)
            next_room = player.current_room.id
            # record where you went
            # traversal graph[prev room][direction] = current room id
            traversal_graph[start_room][direction] = player.current_room.id
            next_paths = player.current_room.get_exits()
            if next_room not in traversal_graph:
                traversal_graph[next_room] = {}
                for pathway in next_paths:
                    traversal_graph[next_room][pathway] = '?'
            # record where you came from 
            # traversal graph[current room][opposite direction] = prev room id 
            traversal_graph[next_room][reverse[direction]] = start_room
            # repeat to dead end
            s.push(next_room)
    # look for the next '?' 
    next_traverse = find_unexplored(player.current_room.id)
    # print("next", next_traverse)
    # recurse
    traverse(next_traverse)
        

def find_unexplored(starting_point):
    # end point is "?", return the shortest path to "?"
    q = Queue()
    # print(traversal_graph)
    q.enqueue(starting_point)


    while q.size() > 0:
        room = q.dequeue()
        # print("match room", room)
        # print("match player", player.current_room.id)
        this_room = {}
        this_room[room] = [traversal_graph[room]]
        explored_room = this_room
        # print("this room?",list(explored_room))

        if room not in explored:
            # print("match room",room)
            for way in explored_room[room]:
                check_list = list(way.values())
                # this seems to have been the issue
                set_check_list = set(check_list)
                # print("check", set_check_list)
                if '?' in set_check_list:
                    return room # this return will give me what I need to traverse again
            explored[room] = list(traversal_graph[room])
            # print("status of explored in bfs",explored)
        if len(current_path) > 0:
            direction = current_path.pop()
            back_track = reverse[direction]
            # print("back_track", back_track)
            player.travel(back_track)
            traversal_path.append(back_track)
            q.enqueue(player.current_room.id)
        # print("traversal", traversal_path)
        # print("current", current_path)
traverse(press_start)
# print("explored", explored)
# print("traversal", traversal_graph)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
