from itertools import permutations
import random
import time
import numpy as np
import json
import brute_force, greedy
import sys

def print_solution(solution, waste, label, items_to_pack, tempo, values=None):
    print('*' * 20)
    print(label)
    print('*' * 20) 
    print(f"Tempo de execução: {tempo}")
    print(f"Itens: {items_to_pack}")
    print(f"Valor obtido: {values}")
    print(f"Número de bins usados: {len(solution)}")

    for i, bin_contents in enumerate(solution):
        print(f"Bin {i + 1}: {bin_contents}")

    print(f"Total waste of this combination: {waste}")


def get_random_array(max_range, n):
    return [random.randint(1, max_range) for _ in range(n)]

def get_random_itens_1d(n, max_range, n_items):
    result = []
    for k in range(n):
        result.append(get_random_array(max_range, n_items))
    return result

def get_random_itens_2d(n, max_range, n_items):
    items = []
    for k in range(n):
        weights = get_random_array(max_range, n_items)
        values = get_random_array(max_range+1000, n_items)

        items.append(list(zip(weights, values)))

    return items

def save_metrics(brute_force_time, greedy_time, metrics_dict, n_loops, n_items, label):
    np.set_printoptions(precision = 2, suppress = True) 

    if brute_force_time:
        print(f"Força bruta: \n\t Media:{np.mean(brute_force_time)} \n\t Min:{np.min(brute_force_time)} \n\t Max:{np.max(brute_force_time)}")
    if greedy_time:
        t = f"{np.mean(greedy_time):.6f}"
        min = f"{np.min(greedy_time):.6f}"
        max = f"{np.max(greedy_time):.6f}"
        print(f"Guloso: \n\t Media:{t} \n\t Min:{min} \n\t Max:{max}")
    
    with open(f"result-{label}-{n_loops}-{n_items}.json", 'w') as arquivo:
        json.dump(metrics_dict, arquivo)
    print("Arquivo  salvo! ")

def run_with_weights():
    capacity = 100
    brute_force_time = []
    greedy_time = []
    n_loops = 30
    n_items = 500000    
    metrics_dict = {}
    items = get_random_itens_1d(n_loops, capacity/2, n_items)     
    i = 0
    metrics_dict[i] = {}

    #print("Running brute force")
    #for items_to_pack in items:

    #    inicio = time.time()
    #    solution, waste = brute_force.run_with_weight(items_to_pack, capacity)
    #    total_time_fmt = f"{time.time()-inicio:.6f}"

    #    print_solution(solution, waste, 'força bruta', items_to_pack, total_time_fmt)
    #    
    #    brute_force_time.append(float(total_time_fmt))
    #    metrics_dict[i]["brute_force"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}


    print("Running greedy")
    for items_to_pack in items:
        print("Iniciando o guloso")
        inicio = time.time()

        solution, waste = greedy.run_with_weight(items_to_pack, capacity)
        total_time_fmt = f"{time.time()-inicio:.6f}"

        print_solution(solution, waste, 'greedy', items_to_pack, total_time_fmt)
        greedy_time.append(float(total_time_fmt))
        metrics_dict[i]["greedy"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}

    save_metrics(brute_force_time, greedy_time, metrics_dict, n_loops, n_items, "with_weight")


def run_with_values():
    capacity = 10
    brute_force_time = []
    greedy_time = []
    n_loops = 30
    n_items = 11 
    metrics_dict = {}
    i = 0
    metrics_dict[i] = {}


    items = get_random_itens_2d(n_loops, capacity/2, n_items)     

    i = 0
    for items_to_pack in items:
        metrics_dict[i] = {}
        print("-"*50)
        print(f"Iteração n {i}")
        print("-"*50)

        ### força bruta ##
        #inicio = time.time()
        #solution, waste = brute_force.run_with_values(items_to_pack, capacity)
        #total_time_fmt = f"{time.time()-inicio:.6f}"

        #print_solution(solution, waste, 'força bruta', items_to_pack, total_time_fmt)
        
        #brute_force_time.append(float(total_time_fmt))
        #metrics_dict[i]["brute_force"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}


        ## greedy ##
        inicio = time.time()
        solution, waste, values = greedy.run_with_values(items_to_pack, capacity)
        total_time_fmt = f"{time.time()-inicio:.6f}"

        print_solution(solution, waste, 'greedy', items_to_pack, total_time_fmt, values=values)
        
        greedy_time.append(float(total_time_fmt))
        metrics_dict[i]["greedy"] = {"itens":items_to_pack, "total_time": total_time_fmt, "waste": waste, "solution":solution}

        i += 1

    save_metrics(brute_force_time, greedy_time, metrics_dict, n_loops, n_items, "with_values")



#run_with_weights()
run_with_values()
