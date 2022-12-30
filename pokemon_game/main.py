import os
from time import sleep
from readchar import readchar


world_map = """\
#########    #############
#       #    #           #
#   A   #    #     R     #
#       #    #           #
#       #    #           #
###   ###    #######     #



#       #    #           #
#       #    #           #
#       #    #           #
#   G   #    #     E     #
#       #    #           #
#########    #############\
"""

X_COORDINATE = 0
Y_COORDINATE = 1

list_of_world_map = [list(row) for row in world_map.split("\n")]
player_position = [10, 0]
trainer_found = False
trainers = ['A', 'R', 'E', 'G']
trainer_name = ''
trainer_position = []
MAP_WIDTH = len(list_of_world_map[0])
MAP_HEIGHT = len(list_of_world_map)

while True:
    os.system("clear")

    if trainer_found:
        trainer_name = 'Arven' if trainer_name == 'A' else 'Riley' if trainer_name == 'R' else 'Ethan' if trainer_name == 'E' else 'Gavin'
        print("You found a trainer!")
        print(f"Hi there! I'm {trainer_name}. I'm a Pokemon trainer.")
        want_fight = input("Do you want to fight? (y/n) ") == "y"

        if want_fight:
            if trainer_name == 'Arven':
                print("I have one Pokemon: Bulbasaur.")

                print("You start the battle with your Pokemon: Pikachu.")

                player_pokemon_health = 50
                trainer_pokemon_health = 70

                while player_pokemon_health > 0 and trainer_pokemon_health > 0:
                    os.system('clear')
                    print("HEALTH")
                    print(f'Bulbasur {"#" * trainer_pokemon_health}')
                    print(f'Pikachu {"#" * player_pokemon_health}')
                    print("What attack do you want to use?")
                    attack = input(
                        " 1. Thunderbolt\n 2. Thunder\n 3. Volt Tackle\n 4. Thunder Shock\n")

                    if attack == '1':
                        trainer_pokemon_health -= 10
                    elif attack == '2':
                        trainer_pokemon_health -= 5
                    elif attack == '3':
                        trainer_pokemon_health -= 8
                    elif attack == '4':
                        trainer_pokemon_health -= 3
                    else:
                        print('Opción inválida')
                        sleep(3)
                else:
                    win = trainer_pokemon_health <= 0

                    if win:
                        list_of_world_map[trainer_position[Y_COORDINATE]
                                          ][trainer_position[X_COORDINATE]] = ' '

                        trainers.remove('A')

                        print('Ganaste')
                        sleep(3)
                    else:
                        print('Perdiste')
                        sleep(3)

                trainer_found = False
            elif trainer_name == 'Riley':
                print("I have three Pokemon: Pidgey, Rattata, and Spearow.")
                list_of_world_map[trainer_position[Y_COORDINATE]
                                  ][trainer_position[X_COORDINATE]] = ' '
                trainers.remove('R')

                input()
                trainer_found = False
            elif trainer_name == 'Ethan':
                print("I have three Pokemon: Caterpie, Weedle, and Pidgey.")
                list_of_world_map[trainer_position[Y_COORDINATE]
                                  ][trainer_position[X_COORDINATE]] = ' '
                trainers.remove('E')
                input()
                trainer_found = False
            elif trainer_name == 'Gavin':
                print("I have three Pokemon: Arcanine, Charizard, and Blastoise.")
                list_of_world_map[trainer_position[Y_COORDINATE]
                                  ][trainer_position[X_COORDINATE]] = ' '
                trainers.remove('G')
                input()
                trainer_found = False
        else:
            trainer_found = False
    else:
        for y in range(len(list_of_world_map)):
            for x in range(len(list_of_world_map[y])):
                if x == player_position[X_COORDINATE] and y == player_position[Y_COORDINATE]:
                    print("P", end=" ")
                else:
                    print(list_of_world_map[y][x], end=" ")

                if list_of_world_map[y][x] in trainers and x == player_position[X_COORDINATE] and y == player_position[Y_COORDINATE]:
                    trainer_name = list_of_world_map[y][x]
                    trainer_position = [x, y]
                    trainer_found = True
            print()

        if len(trainers) == 0:
            os.system('clear')
            print(f'{"*" * 10} GANASTE {"*" * 10}')
            sleep(5)
            break

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
