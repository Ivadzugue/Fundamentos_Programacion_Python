claves = list()
valores = list()
for i in range(0,3):
    clave = input("Digite la clave ")
    valor = input(f"Digite eñ valor {clave} ")
    claves.append(clave)
    valores.append(valor)

variable = dict(zip(claves,valores))
print(variable)