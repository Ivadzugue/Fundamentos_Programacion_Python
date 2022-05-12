diccionario = {
    'Barco': 1,
    'Casa': 2,
    6: False
}

try:
   variable = input("Ingrese la clave del diccionario: ")
   diccionario.pop(variable) 
   print(diccionario)
except KeyError:
    print("Digitó un valor que no existe")