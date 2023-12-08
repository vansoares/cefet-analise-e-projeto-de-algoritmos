from itertools import permutations
import random
import time
import numpy as np


def get_all_permutations(items, length):
    return list(permutations(items, length))

def bruteforce(items_permutations, capacity):
    best_solution = None
    best_waste = 1000

    # percorre todas as combinações de itens
    for p in items_permutations:
        bins = [[]]

        # para cada item da lista
        for item in p:
            # caso o peso do item seja maior que a capacidade do bin
            if item > capacity:
                print("Item is bigger than capacity")
                return [], 0

            #vai adicionando novos bins conforme o necessario
            if len(bins[-1]) > 0:
                bins.append([])

            # percorre todos os bins
            for b in bins:
                #calcula o qunato aidna tem de espaço livre no bin
                bin_content = sum(b)
                free_space = capacity - bin_content

                #se o espaço livre for maior do que o peso do item, adiciona
                # senao passa para o proximo item
                if item <= free_space:
                    b.append(item)
                    break
                else:
                    continue

        # calcula o desperdício de espaço, calculando o espaço livre em todos os bins
        space_waste = sum(capacity - sum(bin_contents) for bin_contents in bins)
        if space_waste < best_waste:
            best_solution = bins
            best_waste = space_waste

    return best_solution, best_waste

def guloso(items, capacity):
    sorted_items = sorted(items)
    bins = [[]]

    for b in bins:
        isNotFull = True

        if len(sorted_items) == 0:
            break

        while isNotFull:
            bin_content = sum(b)
            free_space = capacity - bin_content

            if len(sorted_items) > 0:
                min_item = sorted_items[0]

             # vai adicionando novos bins conforme o necessario
            if len(bins[-1]) > 0:
                bins.append([])

            if min_item <= free_space:
                b.append(min_item)
                sorted_items.remove(min_item)
            else:
                isNotFull = False

    space_waste = sum(capacity - sum(bin_contents) for bin_contents in bins)

    return bins, space_waste


def print_solution(solution, waste, label, itens, tempo):
    print('*' * 20)
    print(label)
    print('*' * 20)
    print(f"Itens analisados: {itens}")
    print(f"Tempo de execução: {tempo}")

    for i, bin_contents in enumerate(solution):
        print(f"Bin {i + 1}: {bin_contents}")

    print(f"Total waste of this combination: {waste}")


def get_random_array(max_range, n):
    return [random.randint(1, max_range) for _ in range(n)]

capacity = 10
brute_force_time = []
guloso_time = []
n_loops = 5
n_items = 10
min_waste_fb = 100000
min_waste_g = 100000


# gerar os mesmos conjuntos de objetos para que os algoritmos possa utilizar
itens_set = []
print("Gerando os conjuntos que serao usados")
for i in range(n_loops):
    itens_set.append(get_random_array(capacity, n_items))

for items_to_pack in itens_set:
    items_permutations = get_all_permutations(items_to_pack, len(items_to_pack))

    inicio = time.time()
    solution, waste = bruteforce(items_permutations, capacity)
    fim = time.time()
    print_solution(solution, waste, 'força bruta', items_to_pack, fim-inicio)
    
    brute_force_time.append(fim-inicio)
    if waste < min_waste_fb:
        min_waste_fb = waste

# guloso
for items_to_pack in itens_set:
    inicio = time.time()

    solution, waste = guloso(items_to_pack, capacity)
    fim = time.time()

    print_solution(solution, waste, 'guloso', items_to_pack, fim-inicio)
    guloso_time.append(fim-inicio)
    if waste < min_waste_g:
        min_waste_g = waste


print(f"Força bruta: \n\t Min waste: {min_waste_fb } \n\t Media:{np.mean(brute_force_time)} \n\t Min:{np.min(brute_force_time)} \n\t Max:{np.max(brute_force_time)}")
print(f"Guloso: \n\t Min waste: {min_waste_g} \n\t Media:{np.mean(guloso_time)} \n\t Min:{np.min(guloso_time)} \n\t Max:{np.max(guloso_time)}")