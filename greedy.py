from itertools import permutations
import random
import time
import numpy as np
import utils

def run_with_weight(items, capacity):
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

    used_bins = []
    for b in bins:
        if len(b) > 0:
            used_bins.append(b)

    space_waste = sum(capacity - sum(bin_contents) for bin_contents in used_bins)

    return used_bins, space_waste


def run_with_values(items, capacity):
    # ordenando de forma reversa porque os valores sao 2x o peso, entao ele tenta pegar os de 
    # maior valor primeiro
    sorted_items = sorted(items, key=lambda x: x[1])

    bins = [[]]
    bins_values = []

    already_used = set()

    for b in bins:
        if len(sorted_items) == 0:
            break

        total_value = 0
        for index, item in enumerate(sorted_items):
            if item in already_used:
                continue

            # Descompacta a tupla em variáveis
            weight, value = item            
            bin_content = utils.calculate_bin_content(b)
            free_space = capacity - bin_content

            if weight <= free_space:
                b.append(item)
                total_value += value
                already_used.add(item)

            else:
                continue


            # vai adicionando novos bins conforme o necessario
            if len(bins[-1]) > 0:
                bins.append([])

        bins_values.append(total_value)

    used_bins = []
    for b in bins:
        if len(b) > 0:
            used_bins.append(b)

    space_waste = utils.get_total_waste(used_bins, capacity)

    return used_bins, space_waste, bins_values
