from itertools import permutations
import random
import time
import numpy as np
import json


def get_all_permutations(items, length):
    return list(permutations(items, length))

def run(items_permutations, capacity):
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

        used_bins = []
        for b in bins:
            if len(b) > 0:
                used_bins.append(b)

        # calcula o desperdício de espaço, calculando o espaço livre em todos os bins
        space_waste = sum(capacity - sum(bin_contents) for bin_contents in used_bins)
        if space_waste < best_waste:
            best_solution = used_bins
            best_waste = space_waste

    return best_solution, best_waste
