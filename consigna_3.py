from jedi import jedis


class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie, ranking):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie
        self.ranking = ranking

# a)
def ordenados(jedi_list):
    sorted_jedi = sorted(jedi_list, key=lambda jedi: (jedi.nombre, jedi.especie))
    for jedi in sorted_jedi:
        print(f"Nombre: {jedi.nombre}, Especie: {jedi.especie}")

# b)
def info(jedi_list, nombres):
    for jedi in jedi_list:
        if jedi.nombre in nombres:
            print(f"Nombre: {jedi.nombre}")
            print(f"Maestros: {jedi.maestros}")
            print(f"Colores de sable de luz: {jedi.colores_sable}")
            print(f"Especie: {jedi.especie}")
            print(f"Ranking: {jedi.ranking}")

# d)
def especie(jedi_list, especies):
    for jedi in jedi_list:
        if jedi.especie.lower() in especies:
            print(f"Nombre: {jedi.nombre}, Especie: {jedi.especie}")

# e)
def letra_a(jedi_list, letra):
    for jedi in jedi_list:
        if jedi.nombre.startswith(letra):
            print(f"Nombre: {jedi.nombre}")

# f)
def mucho_colores(jedi_list):
    for jedi in jedi_list:
        if len(jedi.colores_sable) > 1:
            print(f"Nombre: {jedi.nombre}, Colores de sable: {', '.join(jedi.colores_sable)}")

# g)
def amarillo_o_violetas(jedi_list, colores):
    for jedi in jedi_list:
        if any(color in jedi.colores_sable for color in colores):
            print(f"Nombre: {jedi.nombre}, Colores de sable: {', '.join(jedi.colores_sable)}")

# h) y c)
def discipulos_de_maestros(jedi_list, maestros):
    for jedi in jedi_list:
        if jedi.nombre in maestros:
            padawans = [aprendiz for aprendiz in jedi_list if jedi.nombre in aprendiz.maestros]
            if padawans:
                print(f"Padawans de {jedi.nombre}: {[padawan.nombre for padawan in padawans]}")
            else:
                print(f"{jedi.nombre} no tuvo padawans.")

# i)
def grand_masters(jedi_list):
    for jedi in jedi_list:
        if jedi.ranking.lower() == "grand master":
            print(f"Nombre: {jedi.nombre}, Ranking: {jedi.ranking}")


print("\nordenado por nombre y especie:")
ordenados(jedis)

print("\nInfo de Ahsoka Tano y Kit Fisto:")
info(jedis, ["Ahsoka Tano", "Kit Fisto"])

print("\ndiscipulos de Yoda y Luke Skywalker:")
discipulos_de_maestros(jedis, ["Yoda", "Luke Skywalker"])

print("\nJedi de especie humana y twi'lek:")
especie(jedis, ["humano", "twi'lek"])

print("\nJedi arranca con A:")
letra_a(jedis, "A")

print("\nsable de luz de más de un color:")
mucho_colores(jedis)

print("\nsable de luz amarillo o violeta:")
amarillo_o_violetas(jedis, ["amarillo", "violeta"])

print("\ndiscipulos de Qui-Gon Jinn y Mace Windu:")
discipulos_de_maestros(jedis, ["Qui-Gon Jinn", "Mace Windu"])

print("\nranking de Grand Master:")
grand_masters(jedis)
