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


# Lógica de la reproducción aleatoria de los individuos
def reproduction(individuals):
    new_gen = {}
    av_keys = list(individuals.keys())

    while len(av_keys) > 1:
        x = random.choice(av_keys)
        y = random.choice(av_keys)

        if x == y:
            # print("Son iguales, imposible realizar.")
            continue

        if check_relation(individuals[x], individuals[y]):
            #print(f"Son hermanos/primos ({x}, {y}), imposible realizar.")
            continue

        h1 = []
        h2 = []

        for j in range(0, 20, 1):
            new_genes = (individuals[x]["genes"][j] + individuals[y]["genes"][j]) / 2
            if j % 2 == 0:
                h1.append(math.ceil(new_genes))
                h2.append(math.ceil(new_genes))
            else:
                h1.append(math.floor(new_genes))
                h2.append(math.floor(new_genes))

        new_gen[len(new_gen) + 1] = {"genes": h1, "padres": [x, y],
                                     "abuelos": [individuals[x]["padres"], individuals[y]["padres"]],
                                     "bisabuelos": [individuals[x]["abuelos"], individuals[y]["abuelos"]]}
        new_gen[len(new_gen) + 1] = {"genes": h2, "padres": [x, y],
                                     "abuelos": [individuals[x]["padres"], individuals[y]["padres"]],
                                     "bisabuelos": [individuals[x]["abuelos"], individuals[y]["abuelos"]]}

        av_keys.remove(x)
        av_keys.remove(y)

        print(f"{x} y {y} eliminados. Solo quedan {len(av_keys)}.")

    return new_gen


# Generación de la población inicial
population = generate_pop()

# Contador de generaciones
cont = 1

start = time.time()

# Ciclo while que genera poblaciones hasta que se genere un individuo perfecto
while [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9] not in population.values():
    print(f"Generación {cont}:")
    print(population)
    print("Longitud de la población:", len(population))
    population = reproduction(population)
    cont += 1

print(f"Encontramos al individuo perfecto en la generación {cont}.")

end = time.time()
print(f"Tiempo total: {end - start}")
