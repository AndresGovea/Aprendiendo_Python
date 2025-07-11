
# Una manera de usar lo que se conoce como for each
for letter in "Hello world!":
    print(letter)

# Podemos también utilizar arreglos
amigos = ["Carlos", "Sergio", "Rogelio"]
for amigo in amigos:
    print(amigo)

for index in range(3, 10):
    print(index)

# También podemos usar funciones dentro de range
for friend in range(len(amigos)):
    print(friend)