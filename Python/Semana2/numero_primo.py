"""
funcion que reciba como parametro un numero y retorne si ese es numero primo
"""
def primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(num,"No es primo", n, "es divisor")
            return False
    print(num, "Es primo")
    return True

primo(-5)

def primos(numero:int):
    if numero < 1:
        return f"{numero} no es primo"
    elif numero ==2:
        return f"{numero} Es primo"
    else: 
        for i in range(2, numero):
            if numero % i == 0:
                return f"{numero} No es primo"
        return f"{numero} Es primo"
    
primos(5)            