LAST_NAME = "Basas"
STUDENT_ID = "TUPM-26-3492"
FAVORITE_ARTIST = "Bruno Mars"

SEED_DIGIT = 2
ID_SUM = 26
NAME_LENGTH = 5
ARTIST_LENGTH = 10

department_a = [28, 38, 48, 58, 68]
department_b = [15, 25, 35, 45, 55]

merged = []
i = 0
j = 0
comparisons = 0

while i < len(department_a) and j < len(department_b):
    comparisons += 1

    if department_a[i] <= department_b[j]:
        merged.append(department_a[i])
        i += 1
    else:
        merged.append(department_b[j])
        j += 1

merged.extend(department_a[i:])
merged.extend(department_b[j:])

print("Department A:", department_a)
print("Department B:", department_b)
print("Consolidated Dataset:", merged)

print("Records Before:", len(department_a) + len(department_b))
print("Records After:", len(merged))

print("Comparison Count:", comparisons)
print("Ordering Verification:", merged == sorted(merged))

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")