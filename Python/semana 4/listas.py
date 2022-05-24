#Listas paralelas
#"Relacion entre una lista y otra teniendo encuenta su subindice"

""" 
nombres = list()
edades = list()
for i in range (5):
    nombre = input('Digite el nombre')
    edad = input('Digite edad')
    nombres.append(nombre)
    edades.append(edad)
print (nombres)
print (edades)
"""

#Listas compuestas
"""
posicion = [
    [1, 2, 3, 4],
    [5, [9,10,11], 7, 8]
    ]
valor = posicion[1][1][1]
print(valor)
print(type(valor))
for i in posicion:
    for j in i:
        print(j)
"""

"""
posicion = [
    [1, [9,10,11], 3, 4],
    [5, [9,10,11], 7, 8]
    ]
    
suma = 0
for i in posicion:
    for j in i:
        if type(j) == list:
            valor = sum(j)
            suma += valor
print(suma)
"""

def conversion(x:listas):
    pass