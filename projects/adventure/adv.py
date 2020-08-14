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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# will populate and be the directions to cover the graph
traversal_path = []
# world is a graph, the graph
# map (test_line) 
# print("room_graph", room_graph)
# {0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# print("starting room")
# construct a traversal graph starting in room 0
# just  

# Write a dft to get all the paths
    # in every room write a bfs for a room that has an unvisited path
# write a backtracking algorithm

# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops:
# print("player room id", player.current_room.id)
# print("player get exits", player.current_room.get_exits())
# print("BRUH")

press_start = player.current_room.id
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversal_graph = {}
s = Stack()
s.push(press_start)
limit_break = 0
# travel log loop
# while len(traversal_path) < len(room_graph):

print("path start")
while s.size() > 0:
# track previous room
    print("stack is running")
    if limit_break > 500:
        break
    start_room = s.pop()
    # player current room
    # exits = player.get_exits
    exits = player.current_room.get_exits()
    if start_room not in traversal_graph:
        traversal_graph[start_room] = {}
        for pathway in exits:
            traversal_graph[start_room][pathway] = '?'
    # direction = random n e s w random
    # traverse to room player.travel(direction)
    # filter directions to only be random unexplored
    unexplored_exits = [way for way in traversal_graph[start_room] if traversal_graph[start_room][way] == '?']
    # # if direction == '?' continue you dft
    if len(unexplored_exits) > 0:
        print("unexplored in stack", unexplored_exits)
        direction = random.choice(unexplored_exits)
        # player.travel(direction)
        player.travel(direction)
        traversal_path.append(direction)
        next_room = player.current_room.id
        # record where you went
        # traversal graph[prev room][direction] = current room id
        traversal_graph[start_room][direction] = player.current_room.id
        # may need to if not in my graph here but will try without first
        next_paths = player.current_room.get_exits()
        if next_room not in traversal_graph:
            traversal_graph[next_room] = {}
            for pathway in next_paths:
                traversal_graph[next_room][pathway] = '?'
        # record where you came from 
        # traversal graph[current room][opposite direction] = prev room id 
        # I was in x, went y direction, now in z room
        traversal_graph[next_room][reverse[direction]] = start_room
        # repeat to dead end
        s.push(next_room)
        limit_break += 1
    # else do bfs
    else:
        print(traversal_graph)
        print(player.current_room.id)
        location = player.current_room.id
        q = Queue() 
        q.enqueue(location)

        while q.size() > 0:
            print("queue running")
            if limit_break > 500:
                break        
            current_location = q.dequeue()
            print(traversal_graph[current_location])
            print(player.current_room.get_exits())
            exits = player.current_room.get_exits()
            unexplored_exits = [way for way in traversal_graph[current_location] if traversal_graph[current_location][way] == '?']
            if len(unexplored_exits) < 1:
                direction = random.choice(exits)
                player.travel(direction)
                traversal_path.append(direction)
                print(player.current_room.id)
                next_room = player.current_room.id
                q.enqueue(next_room)
            else:
                print("unexplored", unexplored_exits)
                direction = random.choice(unexplored_exits)
                print(direction)
                player.travel(direction)
                traversal_path.append(direction)
                next_path = player.current_room.id
                s.push(next_path)
            limit_break += 1
             
print("traversal", traversal_graph)


    # bfs
    # check list of unexplored exits
    # if no value == '?'


    # s.push(player.current_room.id)






# look at log, go back until 
# need a travel log, list or dictionary
    # i.e I've gone north from room 1
    # key is room value is traveled direction
    # (1, 'n')
    # recurse

# s = Stack()

# # I DON'T KNOW HOW TO TRACK THE ROOM => See BRUH print above. Finally thought to print it
# while s.size() > 0

# while s.size() > 0:
#     # print(visited)
#     room = s.pop()
#     exits = player.current_room.get_exits()
#     # print("room",room) # room is id... do I want the path?
#     # print(room_graph[room])
#     # print(player.current_room.get_exits())
#     if room not in visited:
#         visited.add(room)
#         # pick a random unexplored direction in the room
#         # use random sampling
#         if len(exits) == 1:
#             direction = exits[0]
#         else:
#             rand_index = random.randint(0, len(exits) - 1)
#             direction = exits[rand_index]
#         print("direction", direction)
#     # append the direction key to traversal_path
#         traversal_path.append(direction)
#         # print(traversal_path)
#         # mark the path as explored
#         if direction not in explored:
#             explored[room] = [direction]
#         print("explored", explored)
#         # travel to that direction
#         player.travel(direction)
#         if player.current_room.id not in visited:
#             s.push(player.current_room.id)
#         else:
#             print(direction)
#             print("turnaround",turn_around[direction])
#             # player.travel(turn_around[direction])
#             find_unexplored = [way for way in exits if way not in explored[player.current_room.id]]
#             print("unexplored", find_unexplored)
#             if len(find_unexplored) > 0:
#                 direction = find_unexplored[0]
#             # else:
#             #     rand_index = random.randint(0, len(exits) - 1)
#             #     direction = exits[rand_index]
#             print("direction in else",direction)
#             explored[room].append(direction)
#             print("room before travel", player.current_room.id)
#             player.travel(direction) # this isn't travelling sometimes
#             print("current room", player.current_room.id)
#             print(visited)
#             s.push(player.current_room.id)
# bfs to nearest unexplored room
# while queue isn't empty
    # if the path is in 
        # return that room
    # get the adjacent rooms

# run the dft again

    # older implementation that did not work lol, but may still be helpful
    # direction = random.something(current_room)
    # direction = random.randint(1, len(room) - 1)
    # command = list(room[direction].keys())
    # print(command)
    # traversal_path.append(command)
    # print(room_graph[direction])
    # s.push(room_graph[direction])


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
