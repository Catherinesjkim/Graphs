"""
Write most of my code here

neighbor: any adjacent room - each room has a function. Get exits. You can use the rooms themselves to figure out where to go next without the player.

Algo:
start from room 0, discover the entire set of rooms. When you go North: populate that value of the room --> Adjacency list. Done if I have 500 keys and no question marks. 

1. Use BFS when stuck to find empty room - not explored yet. Can't find one? Done with searching. If you use player, you might get lost. Do BFS first on all the rooms without the player (Human can't move BFS way). Those are the paths -->

2. Use DFT in general - no more door to go to, at the end of the traversal. You can't teleport from one room to another. Gotta back track from current room to the unvisited room. You need to know when to end or start a traversal. I can use the player here. 

"""
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# if test_loop working, probably main_maze will work
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# makes the rooms to show in a pretty way
world.print_rooms()
print(world.rooms)
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


"""
1. Tests do not pass
2. Tests pass with len(traversal_path) <= 2000 (input)
3. Tests pass with len(traversal_path) < 960 (input)
"""
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
    # print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
    # print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    # print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
        # print("I did not understand that command.")
