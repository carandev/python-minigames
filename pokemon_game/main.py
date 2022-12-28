import os
from readchar import readchar


world_map = """\
#########    #############
#       #    #           #
#       #    #           #
#       #    #           #
#       #    #           #
###   ###    #######     #
                          
                          
                          
#       #    #           #
#       #    #           #
#       #    #           #
#       #    #           #
#       #    #           #
#########    #############\
"""

X_COORDINATE = 0
Y_COORDINATE = 1

list_of_world_map = [list(row) for row in world_map.split("\n")]
player_position = [10, 0]
MAP_WIDTH = len(list_of_world_map[0])
MAP_HEIGHT = len(list_of_world_map)

while True:
    os.system("clear")

    for y in range(len(list_of_world_map)):
        for x in range(len(list_of_world_map[y])):
            if x == player_position[X_COORDINATE] and y == player_position[Y_COORDINATE]:
                print("P", end=" ")
            else:
                print(list_of_world_map[y][x], end=" ")
        print()

    player_move_key = readchar()

    if player_move_key == "w":
        if list_of_world_map[player_position[Y_COORDINATE] - 1][player_position[X_COORDINATE]] != "#":
            player_position[Y_COORDINATE] -= 1
            player_position[Y_COORDINATE] %= MAP_HEIGHT
    elif player_move_key == "s":
        if list_of_world_map[(player_position[Y_COORDINATE] + 1) % MAP_HEIGHT][player_position[X_COORDINATE]] != "#":
            player_position[Y_COORDINATE] += 1
            player_position[Y_COORDINATE] %= MAP_HEIGHT
    elif player_move_key == "a":
        if list_of_world_map[player_position[Y_COORDINATE]][player_position[X_COORDINATE] - 1] != "#":
            player_position[X_COORDINATE] -= 1
            player_position[X_COORDINATE] %= MAP_WIDTH
    elif player_move_key == "d":
        if list_of_world_map[player_position[Y_COORDINATE]][(player_position[X_COORDINATE] + 1) % MAP_WIDTH] != "#":
            player_position[X_COORDINATE] += 1
            player_position[X_COORDINATE] %= MAP_WIDTH
    elif player_move_key == "q":
        print("Thanks for playing!")
        break
