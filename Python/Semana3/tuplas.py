## Definir tuplas
## Son ordenadas
## Son inmutables, no se puede cambiar el valor

from xml.etree.ElementTree import QName


A=()
B = tuple()
print(type(B))
print(type(A))

O = (8,7)
print(O)

P= (8,7,0,12,12)
print(P.count(12)) ##contar cuantas veces esta un elemento
print(len(P)) ##dimension de un elemento

Q = ('nombre', 'Ivonne')
Q[1] = 'Pepito Perez'