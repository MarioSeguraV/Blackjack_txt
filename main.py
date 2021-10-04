import random
import time


def rep():
    card = random.randint(1, 13)
    if card == 11:
        card_val = 10
        print("Tu carta es: J")
    elif card == 12:
        card_val = 10
        print("Tu carta es: Q")
    elif card == 13:
        card_val = 10
        print("Tu carta es: K")
    else:
        card_val = card
        print("Tu carta es:", card_val)
    return card_val


def rep_bot():
    card = random.randint(1, 13)
    if card == 11:
        card_val = 10
        print("J")
    elif card == 12:
        card_val = 10
        print("Q")
    elif card == 13:
        card_val = 10
        print("K")
    else:
        card_val = card
        print(card_val)
    return card_val


def intro():
    print("Bienvenido \n¿Cuál es tu nombre?")
    name = str(input())
    print("\nHola", name, "estas son tus cartas:")
    return name


def extra_rounds():
    print("\n¿Qué quieres hacer? \nEscribe 'h' para recibir otra carta, escribe 's' para quedarte como estás, escribe 'e' para finalizar ")


def final():
    print("\nTotal =", count)


def bot():
    count2 = 0
    count2 += rep_bot()
    end = 0
    while end != 2 and count2 < 21:

        possibility = random.randint(1, 4)

        if possibility == 1 and count2 >= 15:
            end = 2

        elif possibility != 2:
            count2 += rep_bot()
    time.sleep(1)
    print("\nTotal =", count2)
    return count2


def winner(a, b):
    print("")
    if a == 21 and a != b:
        print("QUE SUERTE! GANASTE")

    elif b == 21 and b != a:
        print("QUE SUERTE LA DEL BOT! HA GANADO")

    elif a == b:
        print("BUENO! ES UN EMPATE")

    elif a <= 21 and b <= 21:
        if a > b:
            print("FELICIDADES! HAS GANADO")
        else:
            print("MALA SUERTE! ESTA VEZ EL BOT HA GANADO")

    elif a >= 22 and b < 21:
        print("ESTUVISTE MUY CERCA! ESTA VEZ SE LO LLEVA EL BOT")

    elif a > 21 and b >= 22:
        print("PUES LOS DOS SE PASARON, PERO TIENES SUERTE, ES UN EMPATE!")

    elif a <= 21 and b >= 22:
        print("WOW! GANASTE")

    elif player_try <= 5 and a < 21:
        print("NUNCA HABIAS TENIDO TANTA SUERTE. HAS GANADO!")


# Program
play_again = 1
name1 = intro()
player_try = 0
bot_try = 0

while play_again == 1:
    # Basics
    count = 0
    count += rep()
    count += rep()
    print("Hasta ahora tu total es de:", count)
    # Player's game
    extra_rounds()
    choice = str(input())
    end1 = 0
    while count < 21 and end1 != 2:

        if choice == 'h':
            count += rep()
            print("Hasta ahora tu total es de:", count)
            player_try += 1

        elif choice == 's':
            end1 = 2

        elif choice == 'e':
            print("\nHASTA LA PRÓXIMA '", name1, "'")
            quit()

        if count < 21 and end1 != 2:
            extra_rounds()
            choice = str(input())

    final()

    print("\nLas cartas del bot fueron: ")
    time.sleep(1)

    winner(count, bot())

    time.sleep(1)
    print("\n \n¿Quieres jugar de nuevo? \nTeclea 1 para jugar de nuevo \nTeclea 2 para salir")
    play_again = int(input())
    print("")

print("\nHASTA LA PRÓXIMA '", name1, "'")
quit()
time.sleep(1)
