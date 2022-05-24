#conjuntos

conjunto = {1, 2, 3, 4}
print(conjunto)

conjunto1 = {1, 2, 3, 4, 4}
print(conjunto1)
print(len(conjunto))

#crear conjunto vacio
conjunto = set()

#operaciones de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 6, 3}
#union
u = a | b
print(u)
#interseccion
i = a & b
print(i)
#igualdad
if b == c:
    print('conjuntos iguales')
else:
    print('No son iguales')    
#diferencia 
d = b - a   
e = a - b 
print(d)
print(e)

#adicionar valores a conjuntos
c = (b)
c.add(7)

#conjunto puede ser mutables o inmutables
c = frozenset(b)
print(c)
c.add(7)
