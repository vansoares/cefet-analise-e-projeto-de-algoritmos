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

items_to_pack = [2, 5, 4, 7, 1, 3, 8, 10, 3, 6]
capacity = 10

items_permutations = get_all_permutations(items_to_pack, len(items_to_pack))

solution, waste = bruteforce(items_permutations, capacity)

for i, bin_contents in enumerate(solution):
    print(f"Bin {i + 1}: {bin_contents}")

print(f"Total waste of this combination: {waste}")