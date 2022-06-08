""""
def defiine una función
"""

#return: retorna el valor o la informacion de la función
#print: imprime la informacion indicada

def y(x):
    return x + 1

valor = int(input("ingrese un valor: "))
print(y(valor))

"""
sin return
    1.obtener un valor por teclado y lo convierte a entero
    2.llama a la funcion
    3.print() valor + 1
    4.none   
     
    con return
    1.obtener un valor por teclado y lo convierte a entero
    2.llama a la funcion
    3.enviar a donde fue llamada el valor a return
    4.print() el valor retornado
"""

def y(x):
    if x % 2 == 0: 
        return(f"Si!!, {x} es par")
    else:
        return(f"No!!, {x} no es par")
    
valor = int(input("ingrese un valor: "))
print(y(valor))    

variable = y(x=8)

def z():
    print(variable)

z()    

def valores_opcionales(x=0):
    print(x)
valores_opcionales() 
valores_opcionales(5)   