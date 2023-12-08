from itertools import permutations
import random
import time
import numpy as np
import json
import brute_force, greedy
import sys

def print_solution(solution, waste, label, tempo):
    print('*' * 20)
    print(label)
    print('*' * 20)
    print(f"Tempo de execução: {tempo}")

    for i, bin_contents in enumerate(solution):
        print(f"Bin {i + 1}: {bin_contents}")

    print(f"Total waste of this combination: {waste}")


def get_random_array(max_range, n):
    return [random.randint(1, max_range) for _ in range(n)]

def get_n_random_arrays(n, max_range, n_items):
    result = []
    for k in range(n):
        result.append(get_random_array(max_range, n_items))
    return result

def save_metrics(brute_force_time, greedy_time, metrics_dict):
    print(f"Força bruta: \n\t Media:{np.mean(brute_force_time)} \n\t Min:{np.min(brute_force_time)} \n\t Max:{np.max(brute_force_time)}")
    print(f"Guloso: \n\t Media:{np.mean(greedy_time)} \n\t Min:{np.min(greedy_time)} \n\t Max:{np.max(greedy_time)}")
    with open(f"result-{n_loops}-{n_items}.json", 'w') as arquivo:
        json.dump(metrics_dict, arquivo)
    print("Arquivo  salvo! ")


capacity = 100
brute_force_time = []
greedy_time = []
n_loops = 5
n_items = 9    
metrics_dict = {}
items = get_n_random_arrays(n_loops, capacity-1, n_items)

i = 0
metrics_dict[i] = {}

print("Running brute force")
for items_to_pack in items:

    print("Gerando todas as permutações")
    items_permutations = brute_force.get_all_permutations(items_to_pack, len(items_to_pack))

    inicio = time.time()
    solution, waste = brute_force.run_with_weight(items_permutations, capacity)
    total_time_fmt = f"{time.time()-inicio:.6f}"

    print_solution(solution, waste, 'força bruta', total_time_fmt)
    
    brute_force_time.append(float(total_time_fmt))
    metrics_dict[i]["brute_force"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}


print("Running greedy")
for items_to_pack in items:
    print("Iniciando o guloso")
    inicio = time.time()

    solution, waste = greedy.run_with_weight(items_to_pack, capacity)
    total_time_fmt = f"{time.time()-inicio:.10f}"

    print_solution(solution, waste, 'greedy', total_time_fmt)
    greedy_time.append(float(total_time_fmt))
    metrics_dict[i]["greedy"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}

save_metrics(brute_force_time, greedy_time, metrics_dict)


