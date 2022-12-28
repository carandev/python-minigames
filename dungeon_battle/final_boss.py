# Desafio aritmetico y decisiones con objetos previos

import random
from monster_battle import monster_battle


health = 50
inventory = []
attack = 5

print("Bienvenido al gran juego Dungeon Boss")

name = input("¿Cuál es tu nombre?\n")

print(f"{name.capitalize()} tienes {health} puntos de vida y atacas con {attack} puntos de daño")
print("Estás a dos salones de la sala final")

print("En el primer salón hay un monstruo que te ataca con un ataque de 10 pero si lo derrotas te da una hermosa llave dorada")
print("En el segundo salón hay un monstruo que te ataca con un ataque de 20 pero si lo derrotas te da un sobre con una carta")

option = input("¿Qué salón quieres entrar? (1 o 2)\n")

if option == "1":
    win = monster_battle(health, 20, inventory, attack, 10, 'llave')

    if win:
        first_random_number = random.randint(1, 10)
        second_random_number = random.randint(1, 10)
        operation = 13 * first_random_number + 35 * second_random_number

        print("En la esquina de la sala hay un duende y te dice un enigma")
        print("Si quieres pasar tienes que resolverlo")

        result = input(
            f"¿Cuánto es 13 * {first_random_number} + 35 * {second_random_number}?")

        if int(result) == operation:
            print(
                "Lograste resolver el enigma ahora tienes un orbe de fuego y 20 puntos de vida más")
            health += 20
            inventory.append('orbe')
        else:
            print("No lograste resolver el enigma pero al menos te dan vida")
            health += 10

        print("Ahora puedes entrar a la sala final")
        print("En la sala final hay un monstruo que te ataca con un ataque de 30 pero si lo derrotas te da un anillo")

        win = monster_battle(health, 30, inventory, attack, 30, 'anillo')

        if win:
            print("Para salir debes usar la llave")

            inventory.remove('llave')

            print("\nSaliste de la mazmorra y Has ganado el juego")
        else:
            print("Has perdido el juego")
    else:
        print("Has perdido el juego")
elif option == "2":
    win = monster_battle(health, 20, inventory, attack, 20, 'sobre')

    if win:
        print("El sobre es un hechizo que derrota al jefe y te saca de la mazmorra")
        print("\nHas ganado el juego")
    else:
        print("Has perdido el juego")
