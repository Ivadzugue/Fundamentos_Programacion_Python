#metodo zip()
variable = dict(zip('abcd',[1,2,3,4]))
print(variable)

#diccionario creado con dos litras y metodo zip()
variable = dict(zip(['carro','casa','perro','otro'],[1,2,3]))
print(variable)

#imprime items, valores o llaves de un diccionario
diccionario = {
    'Barco': 1,
    'Casa': 2,
    6: False
}
print( diccionario.items())
print(diccionario.values())
print(diccionario.keys())

#encontrar cuantas veces aparece el numero 2
count = 0
for i in diccionario.values():
    if i == 2:
        count +=1
print(count)        

#borrar elementos
diccionario = {
    'Barco': 1,
    'Casa': 2,
    6: False
}
diccionario.pop(6)
print(diccionario)

#insertar datos a un diccionario
diccionario = {
    'Barco': 1,
    'Casa': 2,
    6: False
}
diccionario['avion'] = False
print(diccionario)

##cambiar valores de un diccionario
diccionario = {
    'Barco': 1,
    'Casa': 2,
    6: False
}
diccionario['Casa'] = 3
print(diccionario)

