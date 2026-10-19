import time

orders = [28, 38, 48, 58, 68, 15, 25, 35]

sorted_input = sorted(orders)
reverse_input = sorted(orders, reverse=True)
random_input = orders.copy()

def bubble_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1

    return a, comparisons, movements

def selection_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a) - 1):
        minimum = i

        for j in range(i + 1, len(a)):
            comparisons += 1

            if a[j] < a[minimum]:
                minimum = j

        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 1

    return a, comparisons, movements

def insertion_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] <= key:
                break

            a[j + 1] = a[j]
            movements += 1
            j -= 1

        a[j + 1] = key

    return a, comparisons, movements

datasets = {
    "Sorted": sorted_input,
    "Reverse": reverse_input,
    "Random": random_input
}

for condition, data in datasets.items():
    print("\n", "=" * 40)
    print("Condition:", condition)
    print("Input:", data)

    for name, algorithm in [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort)
    ]:

        start = time.perf_counter()
        result, comparisons, movements = algorithm(data)
        elapsed = time.perf_counter() - start

        print(f"\n{name}")
        print("Sorted Output:", result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print("Execution Time:", round(elapsed, 8), "seconds")