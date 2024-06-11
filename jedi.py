class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie, ranking):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie
        self.ranking = ranking


#hola profe le pedi a chat q me pase toda la lista jedis a este formato porque sino
# me saltaba un error que no sabia como corregir, espero no haya problema
jedis = [
    Jedi("Ahsoka Tano", ["Anakin Skywalker", "Plo Koon"], ["verde", "azul"], "Togruta", "Padawan"),
    Jedi("Kit Fisto", ["Yoda"], ["verde"], "Nautolano", "Master"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi", "Qui-Gon Jinn"], ["azul"], "Humano", "Jedi Knight"),
    Jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn"], ["azul"], "Humano", "Master"),
    Jedi("Yoda", [], ["verde"], "Desconocida", "Grand Master"),
    Jedi("Luke Skywalker", ["Yoda", "Obi-Wan Kenobi"], ["azul", "verde"], "Humano", "Master"),
    Jedi("Qui-Gon Jinn", [], ["verde"], "Humano", "Master"),
    Jedi("Mace Windu", [], ["violeta"], "Humano", "Master"),
    Jedi("Plo Koon", [], ["azul"], "Kel Dor", "Master"),
    Jedi("Count Dooku", ["Yoda"], ["azul", "rojo"], "Humano", "Sith Lord"),
    Jedi("Rey", ["Luke Skywalker", "Leia Organa"], ["azul"], "Humano", "Jedi Knight"),
    Jedi("Leia Organa", ["Luke Skywalker"], ["azul"], "Humano", "Jedi Knight"),
    Jedi("Ezra Bridger", ["Kanan Jarrus"], ["verde"], "Humano", "Padawan"),
    Jedi("Kanan Jarrus", ["Depa Billaba"], ["azul"], "Humano", "Knight"),
    Jedi("Depa Billaba", [], ["azul"], "Chalactan", "Master"),
    Jedi("Aayla Secura", [], ["azul"], "Twi'lek", "Master"),
    Jedi("Barriss Offee", ["Luminara Unduli"], ["azul"], "Mirialan", "Padawan"),
    Jedi("Luminara Unduli", [], ["verde"], "Mirialan", "Master"),
    Jedi("Shaak Ti", [], ["azul"], "Togruta", "Master"),
    Jedi("Ki-Adi-Mundi", [], ["azul"], "Cerean", "Master"),
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "blanco"], "Togruta", "Padawan"),
    Jedi("Eeth Koth", [], ["azul"], "Zabrak", "Master"),
    Jedi("Bastila Shan", [], ["amarillo"], "Humano", "Padawan"),
    Jedi("Jolee Bindo", [], ["verde"], "Humano", "Padawan"),
    Jedi("Galen Marek (Starkiller)", ["Darth Vader (Anakin Skywalker)"], ["azul", "rojo"], "Humano", "Sith Apprentice"),
    Jedi("Kit Fisto", [], ["verde"], "Nautolano", "Master"),
    Jedi("Ahsoka Tano", ["Anakin Skywalker", "Plo Koon"], ["verde", "azul"], "Togruta", "Padawan"),
    Jedi("Kit Fisto", ["Yoda"], ["verde"], "Nautolano", "Master"),
]