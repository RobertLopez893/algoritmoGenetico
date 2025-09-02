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
        new_pop[i + 1] = {"genes": ind, "padres": None}

    return new_pop


# Lógica de la reproducción aleatoria de los individuos
def reproduction(individuals):
    new_gen = {}
    av_keys = list(individuals.keys())

    while len(av_keys) > 1:
        x = random.choice(av_keys)
        y = random.choice(av_keys)

        if x == y:
            print("Son iguales, imposible realizar.")
            continue

        h1 = []
        h2 = []

        if (individuals[x]["padres"] == individuals[y]["padres"]) and (individuals[x]["padres"] is not None):
            print(f"{x} y {y} son hermanos, imposible realizar.")
            continue

        for j in range(0, 20, 1):
            new_genes = (individuals[x]["genes"][j] + individuals[y]["genes"][j]) / 2
            if j % 2 == 0:
                h1.append(math.ceil(new_genes))
                h2.append(math.ceil(new_genes))
            else:
                h1.append(math.floor(new_genes))
                h2.append(math.floor(new_genes))

        new_gen[len(new_gen) + 1] = {"genes": h1, "padres": [x, y]}
        new_gen[len(new_gen) + 1] = {"genes": h2, "padres": [x, y]}

        av_keys.remove(x)
        av_keys.remove(y)

        print(f"{x} y {y} eliminados. Solo quedan {len(av_keys)}.")

    return new_gen


# Generación de la población inicial
population = generate_pop()

# Contador de generaciones
cont = 1

start = time.time()

while [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9] not in population.values():
    print(f"Generación {cont}:")
    print(population)
    print("Longitud de la población:", len(population))
    population = reproduction(population)
    cont += 1

print(f"Encontramos al individuo perfecto en la generación {cont}.")

end = time.time()
print(f"Tiempo total: {end - start}")
