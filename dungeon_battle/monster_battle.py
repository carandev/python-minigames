
import random


def monster_battle(player_health, monster_health, inventory, player_attack, monster_attack, item):
    win = False
    print(f"Te quedan {player_health} puntos de vida")

    dodge_counter = 0

    while True:
        if player_health <= 0:
            print("Has muerto")
            break
        elif monster_health <= 0:
            print("Has derrotado al monstruo")
            print(f"{item} en el inventario")
            inventory.append(item)
            win = True
            break
        else:
            if 'orbe' in inventory:
                option = input(
                    "¿Deseas atacar y esquivar, solo esquivar o lanzar el orbe? (atacar/esquivar/orbe)\n")
            else:
                option = input(
                    "¿Deseas atacar y esquivar o solo esquivar? (atacar/esquivar)\n")

            if option == "atacar":
                dodge_counter = 0
                random_number = random.randint(1, 3)
                dodge = random_number == 3
                monster_health -= player_attack
                print(f"El monstruo tiene {monster_health} puntos de vida")

                if dodge:
                    print("Esquivaste el ataque del monstruo")
                    print(f"Te quedan {player_health} puntos de vida")
                else:
                    player_health -= monster_attack
                    print("No lograste esquivar el ataque del monstruo")
                    print(f"Te quedan {player_health} puntos de vida")
            elif option == "esquivar":
                if dodge_counter > 4:
                    print("No puedes esquivar más")
                    player_health -= monster_attack
                    print(f"Te quedan {player_health} puntos de vida")
                else:
                    print("Esquivaste el ataque del monstruo")
                    print(f"Te quedan {player_health} puntos de vida")
                    dodge_counter += 1
            elif option == "orbe":
                print('Lanzaste el orbe')
                monster_health -= 20
                print(f"El monstruo tiene {monster_health} puntos de vida")
    return win
