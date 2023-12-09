from itertools import permutations
import random
import time
import numpy as np
import json

def get_all_permutations_tuple(items, length):
    p = permutations(items, length)
    result = []
    for i in p:
        c = []
        for j in i:
            c.append(j)
        result.append(c)

    return result 

def get_all_permutations(items, length):
    return list(permutations(items, length))

def run_with_weight(items, capacity):

    print("Gerando todas as permutações")
    items_permutations = get_all_permutations(items, len(items))

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


def run_with_values(items, capacity):
    best_solution = None
    best_used_bins = 10000
    best_waste = 0

    print("Gerando todas as permutações")
    items_permutations = get_all_permutations_tuple(items, len(items))

    # percorre todas as combinações de itens
    for p in items_permutations:
        bins = [[]]
        already_used = set()

        for b in bins:
            if len(p) == 0:
                break

            # para cada item da lista
            for item in p:
                if item in already_used:
                    continue

                weight, value = item
                # caso o peso do item seja maior que a capacidade do bin
                if weight > capacity:
                    print("Item is bigger than capacity")
                    return [], 0

                #vai adicionando novos bins conforme o necessario
                if len(bins[-1]) > 0:
                    bins.append([])

                # calcula o quanto ainda tem de espaço livre no bin
                bin_content = calculate_bin_content(b)
                free_space = capacity - bin_content

                #se o espaço livre for maior do que o peso do item, adiciona
                # senao passa para o proximo item
                if weight <= free_space:
                    b.append(item)
                    already_used.add(item)
                else:
                    continue

        #remove os bins que não foram preenchidos
        used_bins = []
        for b in bins:
            if len(b) > 0:
                used_bins.append(b)

        # calcula o desperdício de espaço, calculando o espaço livre em todos os bins
        space_waste = get_total_waste(used_bins, capacity)

        if len(used_bins) < best_used_bins:
            best_solution = used_bins
            best_waste = space_waste

    return best_solution, best_waste

def calculate_bin_content(bin):
    bin_content = 0
    for i in bin:
        bin_content += i[0]

    return bin_content

def get_total_waste(bins, capacity):
    waste = 0
    for b in bins:
        bin_content = calculate_bin_content(b)
        waste += capacity - bin_content
    return waste