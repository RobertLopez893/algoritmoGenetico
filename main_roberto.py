# Práctica 2: Generación de Poblaciones

import random
import time
import math


# Función que genera la población inicial con 100 individuos
def generate_pop():
    new_pop = {}

    for i in range(0, 100, 1):
        ind = []
        for j in range(0, 20, 1):
            ind.append(random.randint(1, 9))
        new_pop[i + 1] = {"genes": ind, "padres": None, "abuelos": None, "bisabuelos": None}

    return new_pop


# Verificamos si se encontró al individuo perfecto
def check_goal(individuals):
    for individual in individuals.values():
        if individual["genes"] == [9] * 20:
            return True
    return False


# Evitar el incesto
def check_relation(i1, i2):
    if i1["padres"] and i1["padres"] == i2["padres"]:
        return True

    if i1["abuelos"] and i2["abuelos"]:
        abuelos_i1 = [par for par in i1["abuelos"] if par is not None]
        abuelos_i2 = [par for par in i2["abuelos"] if par is not None]

        if any(par_abuelos in abuelos_i2 for par_abuelos in abuelos_i1):
            return True

    if i1["bisabuelos"] and i2["bisabuelos"]:
        bisabuelos_i1 = [par for sublist in i1["bisabuelos"] if sublist for par in sublist if par is not None]
        bisabuelos_i2 = [par for sublist in i2["bisabuelos"] if sublist for par in sublist if par is not None]

        if any(par_bisabuelos in bisabuelos_i2 for par_bisabuelos in bisabuelos_i1):
            return True

    return False


# Función que efectúa la mutación
def mutation(individual):
    if random.random() < 0.1:
        indexes = random.sample(range(20), 2)
        for idx in indexes:
            individual["genes"][idx] = random.randint(1, 9)
    return individual


# Cruza entre los padres
def cross(p1, p2):
    h1_genes, h2_genes = [], []

    for j, (g1, g2) in enumerate(zip(p1["genes"], p2["genes"])):
        if g1 == 9:
            h1_genes.append(9)
            h2_genes.append(max(g2, random.randint(7, 9)))
        elif g2 == 9:
            h1_genes.append(max(g1, random.randint(7, 9)))
            h2_genes.append(9)
        else:
            new_genes = (g1 + g2) / 2
            val = math.ceil(new_genes) if j % 2 == 0 else math.floor(new_genes)
            h1_genes.append(val)
            h2_genes.append(val)

    return h1_genes, h2_genes


# Evaluación del fitness
def fitness(individual):
    return sum(individual["genes"])


# Lógica de la reproducción con selección del mejor candidato
def reproduction(individuals):
    new_gen = {}
    av_keys = list(individuals.keys())
    random.shuffle(av_keys)

    while len(av_keys) >= 2:
        p1_key = av_keys.pop(0)
        p1 = individuals[p1_key]

        candidates = [key for key in av_keys if not check_relation(p1, individuals[key])]

        p2_key = None
        if candidates:
            p2_key = max(candidates, key=lambda k: fitness(individuals[k]))
        else:
            if av_keys:
                p2_key = av_keys[0]
                print(f"ADVERTENCIA: Forzando reproducción para {p1_key} con {p2_key}.")

        if p2_key:
            p2 = individuals[p2_key]
            av_keys.remove(p2_key)

            h1, h2 = cross(p1, p2)

            child1 = {"genes": h1, "padres": [p1_key, p2_key], "abuelos": [p1["padres"], p2["padres"]],
                      "bisabuelos": [p1["abuelos"], p2["abuelos"]]}
            child2 = {"genes": h2, "padres": [p1_key, p2_key], "abuelos": [p1["padres"], p2["padres"]],
                      "bisabuelos": [p1["abuelos"], p2["abuelos"]]}

            new_gen[len(new_gen) + 1] = mutation(child1)
            new_gen[len(new_gen) + 1] = mutation(child2)

    return new_gen


# Generación de la población inicial
population = generate_pop()

# Contador de generaciones
cont = 1

start = time.time()

# Ciclo while que genera poblaciones hasta que se genere un individuo perfecto
while not check_goal(population):
    print(f"Generación {cont}:")
    print(population)
    print("Longitud de la población:", len(population))
    population = reproduction(population)
    cont += 1

print(f"Generación {cont}:")
print(population)
print("Longitud de la población:", len(population))

print(f"Encontramos al individuo perfecto en la generación {cont}.")

end = time.time()
print(f"Tiempo total: {end - start}")
