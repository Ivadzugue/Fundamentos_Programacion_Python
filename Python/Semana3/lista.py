lista = [1, 'perro', 2, 3, 4, 5, 'cadena', 6, 7]
print (lista)
#las listas son mutables pq puedo cambiar los datos, son ordenados

#dimension de la lista/ cuantos elementos tiene la lista
print(len(lista))

#revanada/ fraccion de la lista
print(lista[1:3])
print(lista[0:-1])
print(lista[2:6])
print(lista[1:])
variable = -2
print(lista[2:variable])

#ACCIONES SOBRE LISTAS
"agrega valores a la lista"
lista.append(2)
print(lista)

"recibir un argumento, y cuenta la cantidad de veces que esta el argumento en la lista"
print(lista.count(2))

"extender una lista agregando un iterable al final"
lista2 = [10, 11, 'gato', 12, 13]
lista.extend(lista2)
print(lista)
lista.extend(lista2[0:1]) 
print(lista)
lista.extend(lista2[0::2])
print(lista)
lista.extend(lista2[0::2])

"posicion de un elemento"
indice = lista.index('cadena')
print(indice)
print(lista[indice])

"como insertar un valor en una posicion especifica"
# lista.insert(indice, objeto)
lista.insert(2, 1.3)
print(lista)