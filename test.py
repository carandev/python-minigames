import os

term_size = os.get_terminal_size()

TERM_WIDTH = term_size.columns
TERM_HEIGHT = term_size.lines

os.system('clear')
border_icon = '*'

room_string = """\
################
#              #
#              #
#              #
#              #
#              #
#######  #######\
"""

room_list = [list(row) for row in room_string.splitlines()]

rooms_position = [
    [int(TERM_WIDTH * 0.1), int(TERM_HEIGHT * 0.1)],
    [int(TERM_WIDTH * 0.7), int(TERM_HEIGHT * 0.1)],
    [int(TERM_WIDTH * 0.1), int(TERM_HEIGHT * 0.7)],
    [int(TERM_WIDTH * 0.7), int(TERM_HEIGHT * 0.7)],
]

draw_room = False

print(border_icon * TERM_WIDTH)

y_continue = False

for y_coordinate in range(TERM_HEIGHT - 2):
    print(border_icon, end='')

    for x_coordinate in range(TERM_WIDTH - 2):

        for first_room_position in rooms_position:
            if x_coordinate == first_room_position[0] and y_coordinate == first_room_position[1]:
                draw_room = True
            elif x_coordinate == first_room_position[0] and y_continue:
                draw_room = True
            elif x_coordinate == len(room_list[0]) + first_room_position[0]:
                draw_room = False

            if draw_room:
                print(room_list[y_coordinate - first_room_position[1]]
                      [x_coordinate - first_room_position[0]], end='')
                break
        if not draw_room:
            print(' ', end='')

    for first_room_position in rooms_position:
        if y_coordinate < len(room_list) + first_room_position[1] and y_coordinate >= first_room_position[1]:
            y_continue = True

        if y_coordinate == len(room_list) + first_room_position[1] - 1:
            y_continue = False

    print(border_icon)

print(border_icon * TERM_WIDTH)
