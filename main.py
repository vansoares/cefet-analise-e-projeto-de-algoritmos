from itertools import permutations


def get_all_permutations(items, length):
    return list(permutations(items, length))


def bruteforce(items_permutations, capacity):
    best_solution = None
    best_waste = 1000

    for p in items_permutations:
        bins = [[] for _ in range(capacity)]

        for item in p:
            if item > capacity:
                print("Item is bigger than capacity")
                return [], 0

            for b in bins:
                bin_content = sum(b)
                free_space = capacity - bin_content

                if item <= free_space:
                    b.append(item)
                    break
                else:
                    continue

        space_waste = sum(capacity - sum(bin_contents) for bin_contents in bins)
        if space_waste < best_waste:
            best_solution = bins
            best_waste = space_waste

    return best_solution, best_waste


def get_min_value(l):
    min_value = 1000
    for value in l:
        if value < min_value:
            min_value = value
    return min_value

def guloso(items, capacity):
    bins = [[] for _ in range(capacity)]

    for b in bins:
        isNotFull = True

        if len(items) == 0:
            break

        while isNotFull:
            bin_content = sum(b)
            free_space = capacity - bin_content

            min_item = get_min_value(items)

            if min_item <= free_space:
                b.append(min_item)
                items.remove(min_item)
            else:
                isNotFull = False

    space_waste = sum(capacity - sum(bin_contents) for bin_contents in bins)

    return bins, space_waste

items_to_pack = [2, 5, 4, 7, 1, 1, 8, 10]
capacity = 10

items_permutations = get_all_permutations(items_to_pack, len(items_to_pack))

# Força bruta
solution, waste = bruteforce(items_permutations, capacity)

print('*'*20)
print('Força bruta')
for i, bin_contents in enumerate(solution):
    print(f"Bin {i + 1}: {bin_contents}")

print(f"Total waste of this combination: {waste}")

# Guloso
solution, waste = guloso(items_to_pack, capacity)

print('*'*20)
print('Guloso')
for i, bin_contents in enumerate(solution):
    print(f"Bin {i + 1}: {bin_contents}")

print(f"Total waste of this combination: {waste}")
