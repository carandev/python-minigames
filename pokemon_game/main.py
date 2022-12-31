import os
import random
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
    player_pokemon_health = 60
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

                trainer_pokemon_health = 45
                pokemon_attacks = [
                    'tackle = 10', 'vine whip = 15', 'razor leaf = 20', 'solar beam = 25']

                while player_pokemon_health > 0 and trainer_pokemon_health > 0:
                    os.system('clear')
                    print("HEALTH")
                    print(f'Bulbasur {"#" * trainer_pokemon_health}')
                    print(f'Pikachu {"#" * player_pokemon_health}')
                    print("What attack do you want to use?")
                    player_attack = input(
                        " 1. Thunderbolt = 20 \n 2. Thunder = 10\n 3. Volt Tackle = 12\n 4. Thunder Shock = 5\n")

                    if player_attack == '1':
                        trainer_pokemon_health -= 20
                    elif player_attack == '2':
                        trainer_pokemon_health -= 10
                    elif player_attack == '3':
                        trainer_pokemon_health -= 12
                    elif player_attack == '4':
                        trainer_pokemon_health -= 5
                    else:
                        print('Opción inválida')
                        sleep(3)

                    pokemon_attack = pokemon_attacks[random.randint(
                        0, len(pokemon_attacks) - 1)]

                    if pokemon_attack == 'tackle = 10':
                        print('Bulbasur used tackle')
                        player_pokemon_health -= 10
                        sleep(1)
                    elif pokemon_attack == 'vine whip = 15':
                        print('Bulbasur used vine whip')
                        player_pokemon_health -= 15
                        sleep(1)
                    elif pokemon_attack == 'razor leaf = 20':
                        print('Bulbasur used razor leaf')
                        player_pokemon_health -= 20
                        sleep(1)
                    elif pokemon_attack == 'solar beam = 25':
                        print('Bulbasur used solar beam')
                        player_pokemon_health -= 25
                        sleep(1)
                    else:
                        print('Opción inválida')
                        sleep(1)

                else:
                    win = trainer_pokemon_health <= 0

                    if win:
                        list_of_world_map[trainer_position[Y_COORDINATE]
                                          ][trainer_position[X_COORDINATE]] = ' '

                        trainers.remove('A')
                        os.system('clear')
                        print('***********')
                        print('* Ganaste *')
                        print('***********')
                        sleep(3)
                    else:
                        print('Perdiste')
                        sleep(3)

                trainer_found = False
            elif trainer_name == 'Riley':
                print("I have one Pokemon: Charmander.")

                print("You start the battle with your Pokemon: Pikachu.")

                player_pokemon_health = 50
                trainer_pokemon_health = 60
                pokemon_attacks = ['scratch = 5', 'ember = 8',
                                   'flamethrower = 12', 'fire blast = 17']

                while player_pokemon_health > 0 and trainer_pokemon_health > 0:
                    os.system('clear')
                    print("HEALTH")
                    print(f'Charmander {"#" * trainer_pokemon_health}')
                    print(f'Pikachu {"#" * player_pokemon_health}')
                    print("What attack do you want to use?")
                    player_attack = input(
                        " 1. Thunderbolt = 20 \n 2. Thunder = 10\n 3. Volt Tackle = 12\n 4. Thunder Shock = 5\n")

                    if player_attack == '1':
                        trainer_pokemon_health -= 20
                    elif player_attack == '2':
                        trainer_pokemon_health -= 10
                    elif player_attack == '3':
                        trainer_pokemon_health -= 12
                    elif player_attack == '4':
                        trainer_pokemon_health -= 5
                    else:
                        print('Opción inválida')
                        sleep(3)

                    pokemon_attack = pokemon_attacks[random.randint(
                        0, len(pokemon_attacks) - 1)]

                    if pokemon_attack == 'scratch = 5':
                        print('Charmander used scratch')
                        player_pokemon_health -= 5
                        sleep(1)
                    elif pokemon_attack == 'ember = 8':
                        print('Charmander used ember')
                        player_pokemon_health -= 8
                        sleep(1)
                    elif pokemon_attack == 'flamethrower = 12':
                        print('Charmander used flamethrower')
                        player_pokemon_health -= 12
                        sleep(1)
                    elif pokemon_attack == 'fire blast = 17':
                        print('Charmander used fire blast')
                        player_pokemon_health -= 17
                        sleep(1)
                    else:
                        print('Opción inválida')
                        sleep(1)

                else:
                    win = trainer_pokemon_health <= 0

                    if win:
                        list_of_world_map[trainer_position[Y_COORDINATE]
                                          ][trainer_position[X_COORDINATE]] = ' '

                        trainers.remove('R')
                        os.system('clear')
                        print('***********')
                        print('* Ganaste *')
                        print('***********')
                        sleep(3)
                    else:
                        print('Perdiste')
                        sleep(3)

                trainer_found = False
            elif trainer_name == 'Ethan':
                print("I have one Pokemon: Squirtle.")

                print("You start the battle with your Pokemon: Pikachu.")

                player_pokemon_health = 50
                trainer_pokemon_health = 60
                pokemon_attacks = ['tackle = 4', 'bubble = 20',
                                   'water gun = 9', 'hydro pump = 12']

                while player_pokemon_health > 0 and trainer_pokemon_health > 0:
                    os.system('clear')
                    print("HEALTH")
                    print(f'Squirtle {"#" * trainer_pokemon_health}')
                    print(f'Pikachu {"#" * player_pokemon_health}')
                    print("What attack do you want to use?")
                    player_attack = input(
                        " 1. Thunderbolt = 20 \n 2. Thunder = 10\n 3. Volt Tackle = 12\n 4. Thunder Shock = 5\n")

                    if player_attack == '1':
                        trainer_pokemon_health -= 20
                    elif player_attack == '2':
                        trainer_pokemon_health -= 10
                    elif player_attack == '3':
                        trainer_pokemon_health -= 12
                    elif player_attack == '4':
                        trainer_pokemon_health -= 5
                    else:
                        print('Opción inválida')
                        sleep(3)

                    pokemon_attack = pokemon_attacks[random.randint(
                        0, len(pokemon_attacks) - 1)]

                    if pokemon_attack == 'tackle = 4':
                        print('Squirtle used tackle')
                        player_pokemon_health -= 4
                        sleep(1)
                    elif pokemon_attack == 'bubble = 20':
                        print('Squirtle used bubble')
                        player_pokemon_health -= 20
                        sleep(1)
                    elif pokemon_attack == 'water gun = 9':
                        print('Squirtle used water gun')
                        player_pokemon_health -= 9
                        sleep(1)
                    elif pokemon_attack == 'hydro pump = 12':
                        print('Squirtle used hydro pump')
                        player_pokemon_health -= 12
                        sleep(1)
                    else:
                        print('Opción inválida')
                        sleep(1)

                else:
                    win = trainer_pokemon_health <= 0

                    if win:
                        list_of_world_map[trainer_position[Y_COORDINATE]
                                          ][trainer_position[X_COORDINATE]] = ' '

                        trainers.remove('E')
                        os.system('clear')
                        print('***********')
                        print('* Ganaste *')
                        print('***********')
                        sleep(3)
                    else:
                        print('Perdiste')
                        sleep(3)

                trainer_found = False
            elif trainer_name == 'Gavin':
                print("I have one Pokemon: Caterpie.")

                print("You start the battle with your Pokemon: Pikachu.")

                player_pokemon_health = 50
                trainer_pokemon_health = 60
                pokemon_attacks = ['tackle = 4', 'string shot = 8',]

                while player_pokemon_health > 0 and trainer_pokemon_health > 0:
                    os.system('clear')
                    print("HEALTH")
                    print(f'Squirtle {"#" * trainer_pokemon_health}')
                    print(f'Pikachu {"#" * player_pokemon_health}')
                    print("What attack do you want to use?")
                    player_attack = input(
                        " 1. Thunderbolt = 20 \n 2. Thunder = 10\n 3. Volt Tackle = 12\n 4. Thunder Shock = 5\n")

                    if player_attack == '1':
                        trainer_pokemon_health -= 20
                    elif player_attack == '2':
                        trainer_pokemon_health -= 10
                    elif player_attack == '3':
                        trainer_pokemon_health -= 12
                    elif player_attack == '4':
                        trainer_pokemon_health -= 5
                    else:
                        print('Opción inválida')
                        sleep(3)

                    pokemon_attack = pokemon_attacks[random.randint(
                        0, len(pokemon_attacks) - 1)]

                    if pokemon_attack == 'tackle = 4':
                        print('Caterpie used tackle')
                        player_pokemon_health -= 4
                        sleep(1)
                    elif pokemon_attack == 'string shot = 8':
                        print('Caterpie used string shot')
                        player_pokemon_health -= 8
                        sleep(1)
                    else:
                        print('Opción inválida')
                        sleep(1)

                else:
                    win = trainer_pokemon_health <= 0

                    if win:
                        list_of_world_map[trainer_position[Y_COORDINATE]
                                          ][trainer_position[X_COORDINATE]] = ' '

                        trainers.remove('G')
                        os.system('clear')
                        print('***********')
                        print('* Ganaste *')
                        print('***********')
                        sleep(3)
                    else:
                        print('Perdiste')
                        sleep(3)

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
