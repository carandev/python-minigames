import os
import random
from readchar import readchar

POS_X = 0
POS_Y = 1


MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]
objects_number = 10
objects_position = []
tail = []
head_symbol = "X"
tail_symbol = "#"


tail_length = 0
objects_to_collect = len(objects_position)

while True:
    os.system("clear")
    print("Use WASD to move")
    print("Press other key to exit")
    print(f"Points: {tail_length}")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    while len(objects_position) < objects_number:
        new_object_position = [random.randint(
            0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_object_position not in objects_position and new_object_position != my_position:
            objects_position.append(new_object_position)

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_print = "   "

            for object_position in objects_position:
                if object_position[POS_X] == coordinate_x and object_position[POS_Y] == coordinate_y:
                    char_to_print = f" O "
                    break
                elif object_position[POS_X] == my_position[POS_X] and object_position[POS_Y] == my_position[POS_Y]:
                    objects_position.remove(object_position)
                    tail_length += 1

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_print = f" {head_symbol} "

            for tail_position in tail:
                if tail_position[POS_X] == coordinate_x and tail_position[POS_Y] == coordinate_y:
                    char_to_print = f" {tail_symbol} "
                if tail_position[POS_X] == my_position[POS_X] and tail_position[POS_Y] == my_position[POS_Y]:
                    print("You died!")
                    os._exit(0)

            print(char_to_print, end="")

        print("|")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    direction = readchar()

    if direction == "w":
        head_symbol = "^"
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        head_symbol = "v"
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        head_symbol = "<"
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        head_symbol = ">"
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    else:
        print("Thanks for playing!")
        break
