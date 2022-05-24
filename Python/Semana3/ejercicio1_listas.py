"""
Agregar 10 valores por teclado 
guardar y mostrar en una lista si los valores son pares
"""
lista =[]
for i in range(10):
    numero = int(input("Escribia un numero entero"))
    lista.append(numero)

print(lista)

lista2=[]
for i in range(10):
    numero = int(input("Escribia un numero entero"))
    if numero %2 == 0:
        lista2.append(numero)
        
print(lista2)     

lista3=[]
control = 0
while control < 10:
    numero = int(input("Escribir un numero entero"))
    if numero %2 ==0:
        lista.append(numero)
        control += 1
print(lista3)        

seguir = 1
lista = list()
while seguir == 1:
    numero = int(input('Agregar nueva valor a la list: '))
    lista.append(numero)
    seguir = int(input('agregar un valor? [1]: '))
print(lista)
