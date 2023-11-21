import readchar
import random
from random import randint
import os

POS_X = 0
POS_Y = 1


obstacle_definition = obstacle_definition = """\
##############################
#       #           #        #
# ####### ##### ##### ####### #
# #     #     # #     #     # #
# # ##### ##### ##### ##### # #
# # #           #           # # 
# # # ### ### ######### ### # #
#   #   # #   #   #   #   #   #
### ##### ### ### ### ##### ###
#   #     #   # #   # #     #  
# # # ##### # # # # # ##### # #
# # #     # # #   # #     # # #
# # ##### # ### ### # ##### # #
# # #   # #       # #   # # # #
# # ### # ######### # ### # # #
# #   # #         # #   # #   #
# ### # ######### # ### ##### #
#                 #           #
##############################\
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]


MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)


my_position = [3, 1]
tail_length = -1
tail = []


# hace el spawn del primer objeto aleatorio

map_objects = [[3, 1]]
contador = 0
# bucle infinito


while True:
    obstacle_positions = []
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if obstacle_definition[y][x] == "#":
                obstacle_positions.append([x, y])

    print(f"Puntuacion: {(tail_length*100)+100}")
    print(tail_length)
    print("-" * (MAP_WIDTH * 3 + 2))

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            object_to_draw = " "

            for map_object in map_objects:
                if (
                    map_object[POS_X] == coordinate_x
                    and map_object[POS_Y] == coordinate_y
                ):
                    object_to_draw = "©"

            for tail_piece in tail:
                if (
                    tail_piece[POS_X] == coordinate_x
                    and tail_piece[POS_Y] == coordinate_y
                ):
                    object_to_draw = "="
            if (
                my_position[POS_X] == coordinate_x
                and my_position[POS_Y] == coordinate_y
            ):
                object_to_draw = "O"

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                object_to_draw = "#"

            print(f" {object_to_draw} ", end="")

        print("|")
    print("-" * (MAP_WIDTH * 3 + 2))

    # si existe un objeto en la misma posicion del objeto este se borra de la lista y ya no se dibuja
    if [my_position[POS_X], my_position[POS_Y]] in map_objects:
        tail_length += 1
        contador += 1
        if contador == 2:
            os.system("cls")
            input("Has ingresado a un combate poquemon contra un Pikachu")
            vida_pikachu = 80
            vida_squirtle = 90

            while vida_squirtle > 0 and vida_pikachu > 0:
                print("Turno de pikachu")
                ataque_pikachu = randint(1, 2)
                if ataque_pikachu == 1:
                    print("pikachu a atacado con Bola Volteo")
                    vida_squirtle -= 10
                else:
                    print("pikachu a atacado con Impactrueno")
                    vida_squirtle -= 11

                if vida_pikachu < 0:
                    vida_pikachu = 0
                if vida_squirtle < 0:
                    vida_squirtle = 0

                barra_pikachu = (vida_pikachu * 10) // 80
                barra_squirtle = (vida_squirtle * 10) // 90
                print(
                    "\nVida del pikachu= ",
                    "[" + barra_pikachu * "#" + (10 - barra_pikachu) * "-" + "]",
                    vida_pikachu,
                    "/80",
                )
                print(
                    "\nVida del squirtle= ",
                    "[" + barra_squirtle * "#" + (10 - barra_squirtle) * "-" + "]",
                    vida_squirtle,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")

                print("Turno Squirtle")

                ataque_squirtle = None
                while ataque_squirtle not in ["A", "P", "B", "N"]:
                    ataque_squirtle = input(
                        "¿Que ataque deseas realizar? Pistola de [A]gua, para [N]ada, [P]lacaje, [B]urbuja: "
                    )
                if ataque_squirtle == "A":
                    print("Squirtle a atacado con Pistola de Agua")
                    vida_pikachu -= 12
                if ataque_squirtle == "P":
                    print("Squirtle a atacado con Placaje")
                    vida_pikachu -= 10
                if ataque_squirtle == "B":
                    print("Squirtle a atacado con Burbuja")
                    vida_pikachu -= 9
                if ataque_squirtle == "N":
                    print("Squirtle No hace nada")
                if vida_pikachu < 0:
                    vida_pikachu = 0
                if vida_squirtle < 0:
                    vida_squirtle = 0

                barra_pikachu = (vida_pikachu * 10) // 80
                barra_squirtle = (vida_squirtle * 10) // 90
                print(
                    "\nVida del pikachu= ",
                    "[" + barra_pikachu * "#" + (10 - barra_pikachu) * "-" + "]",
                    vida_pikachu,
                    "/80",
                )
                print(
                    "\nVida del squirtle= ",
                    "[" + barra_squirtle * "#" + (10 - barra_squirtle) * "-" + "]",
                    vida_squirtle,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")
            if vida_squirtle < vida_pikachu:
                print("pikachu Gano")
                tail_length = 0
                contador -= 1
            else:
                print("Squirtle gano")
        elif contador == 3:
            os.system("cls")
            input("Has ingresado a un combate poquemon contra un Bulbasaur")
            vida_bulbasaur = 70
            vida_squirtle = 90

            while vida_bulbasaur > 1 and vida_squirtle > 1:
                print("Turno de bulbasaur")
                ataque_bulbasaur = randint(1, 2)
                if ataque_bulbasaur == 1:
                    print("bulbasaur a atacado con Latigazo")
                    vida_squirtle -= 10
                else:
                    print("bulbasaur a atacado con Bomba Germen")
                    vida_squirtle -= 11

                if vida_bulbasaur < 0:
                    vida_bulbasaur = 0
                if vida_squirtle < 0:
                    vida_squirtle = 0

                barra_bulbasaur = (vida_bulbasaur * 10) // 80
                barra_squirtle = (vida_squirtle * 10) // 90
                print(
                    "\nVida del bulbasaur= ",
                    "[" + barra_bulbasaur * "#" + (10 - barra_bulbasaur) * "-" + "]",
                    vida_bulbasaur,
                    "/80",
                )
                print(
                    "\nVida del squirtle= ",
                    "[" + barra_squirtle * "#" + (10 - barra_squirtle) * "-" + "]",
                    vida_squirtle,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")

                print("Turno Squirtle")

                ataque_squirtle = None
                while ataque_squirtle not in ["A", "P", "B", "N"]:
                    ataque_squirtle = input(
                        "¿Que ataque deseas realizar? Pistola de [A]gua, para [N]ada, [P]lacaje, [B]urbuja: "
                    )
                if ataque_squirtle == "A":
                    print("Squirtle a atacado con Pistola de Agua")
                    vida_bulbasaur -= 12
                if ataque_squirtle == "P":
                    print("Squirtle a atacado con Placaje")
                    vida_bulbasaur -= 10
                if ataque_squirtle == "B":
                    print("Squirtle a atacado con Burbuja")
                    vida_bulbasaur -= 9
                if ataque_squirtle == "N":
                    print("Squirtle No hace nada")
                if vida_bulbasaur < 0:
                    vida_bulbasaur = 0
                if vida_squirtle < 0:
                    vida_squirtle = 0

                barra_bulbasaur = (vida_bulbasaur * 10) // 80
                barra_squirtle = (vida_squirtle * 10) // 90
                print(
                    "\nVida del bulbasaur= ",
                    "[" + barra_bulbasaur * "#" + (10 - barra_bulbasaur) * "-" + "]",
                    vida_bulbasaur,
                    "/80",
                )
                print(
                    "\nVida del squirtle= ",
                    "[" + barra_squirtle * "#" + (10 - barra_squirtle) * "-" + "]",
                    vida_squirtle,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")
            if vida_squirtle < vida_bulbasaur:
                print("bulbasaur Gano")
                contador -= 1
                tail_length = 1
            else:
                print("Squirtle gano")
        elif contador == 4:
            os.system("cls")
            input("Has ingresado a un combate poquemon contra un Garchomp")
            vida_garchomp = 80
            vida_pikachu = 90

            while vida_pikachu > 1 and vida_garchomp > 1:
                print("Turno de garchomp")
                ataque_garchomp = randint(1, 2)
                if ataque_garchomp == 1:
                    print("garchomp a atacado con Terremoto")
                    vida_pikachu -= 7
                else:
                    print("garchomp a atacado con Carga Dragon")
                    vida_pikachu -= 9

                if vida_garchomp < 0:
                    vida_garchomp = 0
                if vida_pikachu < 0:
                    vida_pikachu = 0

                barra_garchomp = (vida_garchomp * 10) // 80
                barra_pikachu = (vida_pikachu * 10) // 90
                print(
                    "\nVida del garchomp= ",
                    "[" + barra_garchomp * "#" + (10 - barra_garchomp) * "-" + "]",
                    vida_garchomp,
                    "/80",
                )
                print(
                    "\nVida del pikachu= ",
                    "[" + barra_pikachu * "#" + (10 - barra_pikachu) * "-" + "]",
                    vida_pikachu,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")

                print("Turno Pikachu")

                ataque_pikachu = None
                while ataque_pikachu not in ["A", "P", "I", "N"]:
                    ataque_pikachu = input(
                        "¿Que ataque deseas realizar? Pistola de [A]gua, para [N]ada, [P]lacaje, [I]mpactrueno: "
                    )
                if ataque_pikachu == "A":
                    print("Pikachu a atacado con Pistola de Agua")
                    vida_garchomp -= 12
                if ataque_pikachu == "P":
                    print("Pikachu a atacado con Placaje")
                    vida_garchomp -= 10
                if ataque_pikachu == "I":
                    print("Pikachu a atacado con Impactrueno")
                    vida_garchomp -= 15
                if ataque_pikachu == "N":
                    print("Pikachu No hace nada")
                if vida_garchomp < 0:
                    vida_garchomp = 0
                if vida_pikachu < 0:
                    vida_pikachu = 0

                barra_garchomp = (vida_garchomp * 10) // 80
                barra_pikachu = (vida_pikachu * 10) // 90
                print(
                    "\nVida del garchomp= ",
                    "[" + barra_garchomp * "#" + (10 - barra_garchomp) * "-" + "]",
                    vida_garchomp,
                    "/80",
                )
                print(
                    "\nVida del pikachu= ",
                    "[" + barra_pikachu * "#" + (10 - barra_pikachu) * "-" + "]",
                    vida_pikachu,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")
            if vida_pikachu < vida_garchomp:
                print("garchomp Gano")
                contador -= 1
                tail_length = 2
            else:
                print("Pikachu gano")
        elif contador == 5:
            os.system("cls")
            input("Has ingresado a un combate Pokémon contra un Rayquaza")
            vida_rayquaza = 90
            vida_garchomp = 90

            while vida_garchomp > 1 and vida_rayquaza > 1:
                print("Turno de Rayquaza")
                ataque_rayquaza = randint(1, 4)
                if ataque_rayquaza == 1:
                    print("Rayquaza ha atacado con Poder antiguo")
                    vida_garchomp -= 7
                else:
                    print("Rayquaza ha atacado con Air Ace")
                    vida_garchomp -= 9

                if vida_rayquaza < 0:
                    vida_rayquaza = 0
                if vida_garchomp < 0:
                    vida_garchomp = 0

                barra_rayquaza = (vida_rayquaza * 10) // 90
                barra_garchomp = (vida_garchomp * 10) // 90
                print(
                    "\nVida de Rayquaza = ",
                    "[" + barra_rayquaza * "#" + (10 - barra_rayquaza) * "-" + "]",
                    vida_rayquaza,
                    "/80",
                )
                print(
                    "\nVida de Garchomp = ",
                    "[" + barra_garchomp * "#" + (10 - barra_garchomp) * "-" + "]",
                    vida_garchomp,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")

                print("Turno Garchomp")

                ataque_garchomp = None
                while ataque_garchomp not in ["T", "C", "A", "E"]:
                    ataque_garchomp = input(
                        "¿Qué ataque deseas realizar? [T]erremoto, [C]arga Dragon, C[O]la Drafon, [N]ada: "
                    )
                if ataque_garchomp == "T":
                    print("Garchomp ha atacado con Terremoto")
                    vida_rayquaza -= 12
                if ataque_garchomp == "C":
                    print("Garchomp ha atacado con Carga Dragón")
                    vida_rayquaza -= 15
                if ataque_garchomp == "O":
                    print("Garchomp ha atacado con Cola Dragón")
                    vida_rayquaza -= 10
                if ataque_garchomp == "N":
                    print("Garchomp No hace nada")
                if vida_rayquaza < 0:
                    vida_rayquaza = 0
                if vida_garchomp < 0:
                    vida_garchomp = 0

                barra_rayquaza = (vida_rayquaza * 10) // 90
                barra_garchomp = (vida_garchomp * 10) // 90
                print(
                    "\nVida de Rayquaza = ",
                    "[" + barra_rayquaza * "#" + (10 - barra_rayquaza) * "-" + "]",
                    vida_rayquaza,
                    "/90",
                )
                print(
                    "\nVida de Garchomp = ",
                    "[" + barra_garchomp * "#" + (10 - barra_garchomp) * "-" + "]",
                    vida_garchomp,
                    "/90",
                )

                input("\nEnter\n")
                os.system("cls")

            if vida_garchomp < vida_rayquaza:
                print("Rayquaza Gano")
                contador -= 1
                tail_length = 3
            else:
                print("Garchomp gano")

        map_objects.remove([my_position[POS_X], my_position[POS_Y]])
        # Si un objeto quiere hacer spawn en algun lugar de la serpiente se lo recoloca
        while True:
            random_object = [random.randint(2, 19), random.randint(2, 14)]
            if random_object not in tail and random_object not in obstacle_positions:
                map_objects.append(random_object)
                break

    # GAME OVER
    if tail_length == 4:
        print("-" * (MAP_WIDTH * 3 + 2))
        print(
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
            "  GANASTE  ",
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
        )
        print("-" * (MAP_WIDTH * 3 + 2))
        break

    """
        CODIGO PARA MUERTE POR CHOQUE CON COLA
        if [my_position[POS_X], my_position[POS_Y]] in tail:
        print("-" * (MAP_WIDTH * 3 + 2))
        print(
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
            "GAME  OVER",
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
        )
        print("-" * (MAP_WIDTH * 3 + 2))
        break
    """
    direction = readchar.readchar()
    new_position = None
    # movimiento del personaje
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        print("-" * (MAP_WIDTH * 3 + 2))
        print(
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
            "SALIENDO",
            "-" * ((MAP_WIDTH * 3 - 9) // 2),
        )
        print("-" * (MAP_WIDTH * 3 + 2))
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position
    os.system("cls")
