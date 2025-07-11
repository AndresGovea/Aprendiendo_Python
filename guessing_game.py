palabra_secreta = "Hello world!"
palabra = ""
intento = 0
INTENTOS = 3
fuera_de_rango = False 
while palabra_secreta != palabra and not(fuera_de_rango):
    if intento < INTENTOS:
        palabra = input("Dame la palabra: ")
        intento += 1
    else:
        fuera_de_rango = True

if fuera_de_rango:
    print("¡Perdiste!")
else:
    print("¡Ganaste!")
