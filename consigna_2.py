#2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
#a) Contar cuantas especies hay;
#b) Determinar cuantos descubridores distintos hay;
#c) Mostrar todos los dinosaurios que empiecen con T;
#d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
#e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

from dino import dinosaurios

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)



def especies():
    especies = set()
    for dinosaur in dinosaurios:
        especies.add(dinosaur["especie"])
    return len(especies)

def descubridores():
    descubridores = set()
    for dinosaur in dinosaurios:
        descubridores.add(dinosaur["descubridor"])
    return len(descubridores)

def dinosaurios_T():
    for dinosaur in dinosaurios:
        if dinosaur["nombre"].startswith("T"):
            print(dinosaur["nombre"])

def dinosaurios_ligeros():
    for dinosaur in dinosaurios:
        peso = int(dinosaur["peso"].split()[0])
        if peso < 275:
            print(dinosaur["nombre"])


pila_dinosaurios = Stack()

def por_letra(pila, letras):
    for dinosaur in dinosaurios:
        if dinosaur["nombre"][0].upper() in letras:
            pila.push(dinosaur)


print("Cantidad de especies:", especies())
print("Cantidad de descubridores distintos:", descubridores())

print("empiezan con T:")
dinosaurios_T()

print("pesan menos de 275 kg:")
dinosaurios_ligeros()

print("empiezan con A, Q o S:")
letras = {'A', 'Q', 'S'}
por_letra(pila_dinosaurios, letras)
while pila_dinosaurios.size() > 0:
    print(pila_dinosaurios.pop()["nombre"])
