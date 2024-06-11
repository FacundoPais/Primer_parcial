#Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un
#parámetro que es la lista de elementos.

lista = [10,9,8,7,6,5,4,3,2,1,0]

def invertir(lista):
    if len(lista) <= 1:
        return lista
    return [lista[-1]] + invertir(lista[:-1])

print(invertir(lista))