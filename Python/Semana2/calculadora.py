"""
Escribir una función que simule una calculadora científica que permita 
calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
La función preguntará al usuario el valor y la función a aplicar, 
y mostrará por pantalla una tabla con los enteros 
de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""
"""libreria de python con todo el tema de operacione matematicas 'math.pyi'"""
"""import math"""
from math import sin, cos, tan, exp, log
""""creacion diccionario  """
def calculadora(f:str, n:int):
    funciones  = {
        "seno" : sin,
        "coseno" : cos,
        "tangente" : tan,
        "exponencial": exp,
        "log" : log
    }
    resultado = dict()
    operacion = funciones[f]
    for i in range(1,n+1):
        resultado[i] = operacion(i)
    return resultado

def main():
    f = input("Digite la operacion a realizar (seno, coseno, tangente, exponencial, log): ")
    n = int(input("Ingrese un numero entero positivo: "))
    print(calculadora(f,n))
    
main()    