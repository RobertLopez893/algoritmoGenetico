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
        h1 = []
        h2 = []

        x = random.choice(av_keys)

        y = random.choice(av_keys)

        if (individuals[x]["padres"] == individuals[y]["padres"]) and (individuals[x]["padres"] and individuals[y]["padres"] is not None):
            continue

        flag = 0
        for j in range(0, 20, 1):
            if flag % 2 == 0:
                h1.append(math.ceil(((individuals[x][j] + individuals[y][j]) / 2)))
                h2.append(math.ceil(((individuals[x][j] + individuals[y][j]) / 2)))
            else:
                h1.append(math.floor(((individuals[x][j] + individuals[y][j]) / 2)))
                h2.append(math.floor(((individuals[x][j] + individuals[y][j]) / 2)))

        del individuals[x]
        del individuals[y]

        new_gen[len(new_gen) + 1] = h1
        new_gen[len(new_gen) + 1] = h2

        av_keys.remove(x)
        av_keys.remove(y)

    return new_gen


# Generación de la población inicial
population = generate_pop()

# Contador de generaciones
cont = 1

start = time.time()

#while [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9] not in population.values():
for i in range(0, 10, 1):
    print(f"Generación {cont}:")
    print(population)
    print("Longitud de la población:", len(population))
    population = reproduction(population)
    cont += 1

end = time.time()
print(f"Tiempo total: {end - start}")
