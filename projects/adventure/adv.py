from room import Room
from player import Player
from world import World
from map_graph import Map

import os
dirpath = os.path.dirname(os.path.abspath(__file__))
# map_file = dirpath + "/maps/main_maze.txt"

import random
from ast import literal_eval
from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = dirpath + "/maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
# s = Stack()
s = Stack()
visited_rooms = set()
explored_paths = set()
s.push(room_graph[0])
# I need to track the room I'm in
# # I DON'T KNOW HOW TO TRACK THE ROOM 
# while s.size() > 0


# my raw try MAY HAVE TO BE SCRAPPED, WILL HAVE TO START FROM SCRATCH
while s.size() > 0:
    room = s.pop()
    print(room)
    # pick a random unexplored direction in the room
    # use random sampling
    # direction = random.something(current_room)
    direction = random.randint(1, len(room) - 1)
    command = list(room[direction].keys())
    # print(command)
    # append the direction key to traversal_path
    traversal_path.append(command)
        # mark the path as explored
        # travel to that direction
    print(room_graph[direction])
    # s.push(room_graph[direction])
    
# bfs to nearest unexplored room
# while queue isn't empty
    # if the path is in 
        # return that room
    # get the adjacent rooms

# run the dft again





    # paths = s.pop()
    # room = paths[-1]

    # if room not in visited:
        # we want a key and a value
        # explored[room] = paths
        
        # # get neighbors (get friends)
        # for friend in self.friendships[v]:
        #     path_copy = list(path) # can also do path.copy()
        #     path_copy.append(friend)
        #     q.enqueue(path_copy)



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
