amigos = ['Mcree','Bob', 'Ashe', 'Rick']
amigos[2] = 'ashe'
print(amigos[2])

numeros = [2, 3, 4, 9, 12, 1, 0, -1, 1]

# Con la función extend() podemos concatenar dos listas
numeros.extend(amigos)
print(numeros)

# Con la función append() podemos agregar otro elemto al final de la lista
amigos.append('Sergio')
print(amigos)

# Con la función insert() podemos agregar un elemento en el índice que nosotros queramos

amigos.insert(1, 'Mercy') 
print(amigos)

# Con la función remove() podemos eliminar cualquier elemento de una lista

amigos.remove('Sergio')
print(amigos)
numeros.remove(0)
print(numeros)

# La funcion clear() nos ayuda a eliminar todos los elemntos

frutas = ['manzana', 'plátano', 'aguacate']
print(frutas)
frutas.clear()
print(frutas)

# La función pop() nos ayuda a elminar el último elemento de la lista

amigos.pop()
print(amigos)

# Con la función count() podemos contar el númeor de elementos que se repiten

print(numeros.count(1))

# Con la función sort() puedes ordenar la lista, no funciona si la lista tiene tipos de datos diferentes

numeros.clear()
numeros = [2, 3, 4, 9, 12, 1, 0, -1, 1]
numeros.sort()
print(numeros)

# Con la función reverse() puedes invertir la posición de los elementos

numeros.reverse()
print(numeros)

# Si queremos copiar la lista, podemos solo usar la función copy 

amigos2 =  amigos.copy()
print(amigos2)