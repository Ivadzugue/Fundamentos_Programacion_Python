"""
piedra papel o tijera
"""
import random

## piedra papel o tijera
"""     
            PIEDRA  PAPEL TIJERA    <-- fila
   PIEDRA      0      -1     1        0 es empate
   PAPEL       1       0    -1        1 gana columna
   TIJERA     -1       1     0       -1 gana fila
"""
lista1 = ["piedra", "papel", "tijera"]
resultado=[[0,-1,1], [1,0,-1], [-1,1,0]]
ganador={
        0 : "EMPATE",
        1 : "Gana la máquina",
        -1: "Gana el rival"}
seguir = True  ##seguir =1
while seguir:   ##== 1:
    maq = random.randint(0,2)
    print(f"La maquina ha jugado {lista1[maq]} ")
    riv = random.randint(0,2)
    print(f"El rival   ha jugado {lista1[riv]} ")
    res = resultado[maq][riv]    
    print(ganador[res]) 
    ##seguir = int(input('1 para continuar: '))
    seguir = 'S' == input("Desea continuar? S/N ")
