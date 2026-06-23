# BINARY CLUE INVESTIGATOR

# PART 1  
a = 7
b = 7
print("PART 1")
print("a =", a)
print("b =", b)
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)
if (a ^ b) == 0:
    print("Both numbers are equal")
else:
    print("Both numbers are different")

# PART 2
clues = [3, 5, 3, 5, 9]
xor_result = 0
for clue in clues:
    xor_result = xor_result ^ clue 
print("PART 2")
print("Clues:", clues)
print("Final XOR Result:", xor_result)
print("Repeated clues cancel out, so the remaining clue is:", xor_result)

# PART 3
numbers = [4, 7, 4, 2, 7, 2, 9]
odd_number = 0
for number in numbers:
    odd_number = odd_number ^ number
print("PART 3")
print("Numbers:", numbers)
print("Odd-occurring number:", odd_number)

# PART 4
pair_numbers = [3, 9, 3, 5, 5, 7]
xor_of_two = 0
for number in pair_numbers:
    xor_of_two = xor_of_two ^ number
print("PART 4")
print("Numbers:", pair_numbers)
print("XOR of two odd-occurring numbers:", xor_of_two)

# PART 5
rightmost_set_bit = xor_of_two & -xor_of_two
first_odd = 0
second_odd = 0
for number in pair_numbers:
    if number & rightmost_set_bit:
        first_odd = first_odd ^ number
    else:
        second_odd = second_odd ^ number
print("PART 5")
print("Rightmost set bit:", rightmost_set_bit)
print("First odd-occurring number:", first_odd)
print("Second odd-occurring number:", second_odd)
 