from itertools import permutations
import random
import time
import numpy as np
import json

def run(items, capacity):
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


