from itertools import permutations
import random
import time
import numpy as np
import json


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

            if min_item <= free_space:
                b.append(min_item)
                if len(sorted_items) > 0:
                    sorted_items.remove(min_item)
            else:
                isNotFull = False

            # vai adicionando novos bins conforme o necessario
            if len(bins[-1]) > 0:
                bins.append([])

    space_waste = sum(capacity - sum(bin_contents) for bin_contents in bins)

    return bins, space_waste


def print_solution(solution, waste, label, itens, tempo):
    print('*' * 20)
    print(label)
    print('*' * 20)
    print(f"Tempo de execução: {tempo}")

    for i, bin_contents in enumerate(solution):
        print(f"Bin {i + 1}: {bin_contents}")

    print(f"Total waste of this combination: {waste}")


def get_random_array(max_range, n):
    return [random.randint(1, max_range) for _ in range(n)]


capacity = 100
brute_force_time = []
greedy_time = []
n_loops = 3
n_items = 600000
metrics_dict = {}


for i in range(n_loops):
    print("#"*50)
    items_to_pack = get_random_array(53, n_items)
    #print(f"Itens: {items_to_pack}")
    metrics_dict[i] = {}

    #################### força bruta
    #print("Gerando todas as permutações")
    #items_permutations = get_all_permutations(items_to_pack, len(items_to_pack))

    #print("Iniciando o força bruta")
    #inicio = time.time()
    #solution, waste = bruteforce(items_permutations, capacity)
    #total_time = time.time()-inicio
    #total_time_fmt = f"{total_time:.6f}"

    #print_solution(solution, waste, 'força bruta', items_to_pack, total_time_fmt)
    
    #brute_force_time.append(total_time)
    #metrics_dict[i]["brute_force"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}

    #################### guloso
    print("Iniciando o guloso")
    inicio = time.time()

    solution, waste = guloso(items_to_pack, capacity)
    total_time = time.time()-inicio
    total_time_fmt = f"{total_time:.6f}"

    #print_solution(solution, waste, 'greedy', items_to_pack, total_time_fmt)
    greedy_time.append(total_time)
    #metrics_dict[i]["greedy"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}




#print(f"Força bruta: \n\t Media:{np.mean(brute_force_time)} \n\t Min:{np.min(brute_force_time)} \n\t Max:{np.max(brute_force_time)}")
print(f"Guloso: \n\t Media:{np.mean(greedy_time)} \n\t Min:{np.min(greedy_time)} \n\t Max:{np.max(greedy_time)}")
#with open(f"result-{n_loops}-{n_items}.json", 'w') as arquivo:
#    json.dump(metrics_dict, arquivo)
#print("Arquivo  salvo! ")
