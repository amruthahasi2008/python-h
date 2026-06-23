# BINARY SUBSET BUILDER
items = ["A", "B", "C"]
n = len(items)
total_subsets = 2 ** n
print("BINARY SUBSET BUILDER")
print("Items:", items)
print("Number of items:", n)
print("Total subsets: 2 ^", n, "=", total_subsets)

# PART 1 
print("PART 1")
print("For", n, "items, we can create", total_subsets, "subsets.")

# PART 2
print("PART 2")
mask = 0
while mask < total_subsets:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print("Mask", mask, "-> [C][B][A] =", bit2, bit1, bit0)
    mask = mask + 1

# PART 3 
print("PART 3")
sample_mask = 5#Binary: 101
print("Sample Mask:", sample_mask)
print("Binary:", bin(sample_mask))
j = 0
while j < n:
    probe = 1 << j
    if sample_mask & probe:
        print("Bit", j, "is set, so item", items[j], "is selected.")
    else:
        print("Bit", j, "is not set, so item", items[j], "is not selected.")
    j = j + 1

# PART 4
print("PART 4")
mask = 0
while mask < total_subsets:
    subset = []
    j = 0
    while j < n:
        probe = 1 << j
        if mask & probe:
            subset.append(items[j])
        j = j + 1
    print("Mask", mask, "->", subset)
    mask = mask + 1

# PART 5
def bit_difference(a, b):
    difference_count = 0
    while a > 0 or b > 0:
        last_bit_a = a & 1
        last_bit_b = b & 1
        if last_bit_a != last_bit_b:
            difference_count = difference_count + 1
        a = a >> 1
        b = b >> 1
    return difference_count
print("PART 5")
print("Difference between 12 and 15:", bit_difference(12, 15))
print("12 =", bin(12), "15 =", bin(15))
print("Difference between 21 and 24:", bit_difference(21, 24))
print("21 =", bin(21), "24 =", bin(24))
print("Difference between 8 and 8:", bit_difference(8, 8))
print("8 =", bin(8), "8 =", bin(8))
