""""
Summary
    nivel basico

    La formula para calcular un area de un circulo se define como: area = pi x radio¨2 
    para este problema consideramos pi = 3.14159

    calcular el area usando la formula dada en la descripcion del problema
"""
#Variables: no deben empezar por numero, no se puede utilizar palabras claves(def, num, if, while, for)
#El nombre de la variable debe dar informacion del contenido de la variable5
#Import keyword  ---- print(keyword.kwlist)   para validar palabras reservadas 

#Operadores tienen gerarquia: (), signo, potencia, producto y division, Div-modulo, suma y resta, concatenacion, relacionales, negacion

#Errores de sintaxis: estamos no cumpliendo las reglas de escritura y ejecucion del lenguaje
#Errores de semantica: interpretacion del programador al interpretar el programa

PI = 3.14159
radio = float(input ("Digite el valor del radio "))
area = PI * (radio**2) 

#template literals
print (f"El area del circulo con radio {radio} es {area}") 
#concatenacion
print ("El area del circulo con radio " + str(radio) + " es " + str(area))
print ("El area del circulo con radio", radio, "es", area)
print ("El area del circulo con radio %s es %s" %(radio, area))
