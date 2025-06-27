from math import *
# Pintamos en terminal
print('Hello world!')

# Guardamos contenido en un variable
hace = 'Hola Que Hace'

# Volvemos el contenido a mayúsculas
print(hace.upper())

# Volvemos el contenido a minúsculas
print(hace.lower())

# La función index nos devuelve el primer carácter
print(hace.index('Q'))

# Agarramos el quinto carácter de nuestra variable
print(hace[5])

# La función len() nos devuelve la longitud en caracteres de la variable
print(len(hace))

# Guardamos un número a la variable numero
numero = 5

# Convertimos el número a string
print(str(numero))

# L afunción abs() nos na el valor absoluto de la variable
negativo = -5
print(abs(negativo))

# La función pow(,) nos va dar el número elevado a tal número, pow(,,) podemos poner también un módulo 
print(pow(numero, 2)) # 5 al cuadrado = 25
print(pow(numero, 2)) # 5 al cuadrado módulo 4 = 1

# La función max(,) nos dará el número mas grande
print(max(numero, negativo, 3, 4 ,8))

# La función min nos dará el valor mínimo de los númoer que pasemos
print(min(numero, negativo, 3, 4, 8))

"""
La función round() nos da el entero redondeado positivo si es mayor a .5 
y si es menor a .5 nos da el entero mas pequeño.
Si termina en .5 nos dará el número par mas cercano.
Si usamos round(,) nos dará l número pero solo hasta ciertos decimales
"""
print(round(3.5))
print(round(4.56565, 4))

# Las funciones ceil() and floor() nos dan el valor de entero de acuerdo mas grande o mas pequeño

print(ceil(3.5))
print(floor(3.5))

#la funcion sqrt() nos va a dar la raíz cuadrada de cualquier valor que le pasemos

print(sqrt(2))