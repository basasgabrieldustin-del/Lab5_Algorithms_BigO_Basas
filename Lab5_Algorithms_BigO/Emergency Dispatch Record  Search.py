LAST_NAME = "Basas"
STUDENT_ID = "TUPM-26-3492"
FAVORITE_ARTIST = "Bruno Mars"

SEED_DIGIT = 2
ID_SUM = 26
ARTIST_SUM = 151

records = [26, 36, 46, 56, 66, 76, 86, 96]

rotation = SEED_DIGIT
rotated = records[rotation:] + records[:rotation]

target = (ID_SUM + ARTIST_SUM) % 100

comparisons = 0
position = -1

for i, value in enumerate(rotated):
    comparisons += 1
    if value == target:
        position = i
        break

print("Original Dataset:", records)
print("Rotated Dataset:", rotated)
print("Target Incident:", target)

if position != -1:
    print("Found at index:", position)
else:
    print("Target not found")

print("Comparison Count:", comparisons)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")