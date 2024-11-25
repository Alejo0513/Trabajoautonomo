import random

def obtener_palabra_aleatoria():
    palabras=!["perro","marciano","casa","ecuador","verde","arroz"]
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)        
