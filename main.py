import random
import time

def intro():
    print("Bienvenido cuál es tu nombre: ")
    name = str(input())
    return name


def repartir():
    carta = random.randint(1,13)
    if carta == 1:
        print("A")
    elif carta == 11:
        print("J")
    elif carta == 12:
        print("Q")
    elif carta == 13:
        print("K")
    else:
        print(carta)
    return carta


def total():
    cuenta += repartir()
    print("Total =", cuenta)
    return cuenta


def decision():
    print("\n¿Qué quieres hacer? \nEscribe 'h' para recibir otra carta, escribe 's' para quedarte como estás, escribe 'e' para finalizar ")
    dec = str(input())
    if dec == 'h':
        repartir()


print("\nHola", intro(), "tus cartas son:")
repartir()
repartir()
total()
decision()
