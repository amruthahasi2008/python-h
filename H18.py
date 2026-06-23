switch_value = 45   # Binary: 101101
def show_bits(number):
    return bin(number)[2:]
print("MY SMART SWITCH BIT MONITOR")
print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))

# PART 1
binary_value = show_bits(switch_value)
set_bits = binary_value.count("1")
zero_bits = binary_value.count("0")
print("PART 1")
print("Set Bits / ON Switches:", set_bits)
print("Zero Bits / OFF Switches:", zero_bits)

# PART 2 
count = 0
temp = switch_value
while temp > 0:
    if temp & 1:
        count = count + 1
    temp = temp >> 1

print("PART 2")
print("Number of ON switches:", count)

# PART 3 
position = 1
temp = switch_value

while temp > 0:
    if temp & 1:
        break
    position = position + 1
    temp = temp >> 1

print("PART 3")
print("First ON switch is at position:", position)

# PART 4 
print("PART 4")
for i in range(6):
    mask = 1 << i
    print("Bit", i, "Mask:", mask, "Binary:", show_bits(mask))

# PART 5
switch_names = ["Living Room Light","Fan", "Air Conditioner","Door Lock","Garden Light","Security Camera"]
print("PART 5")
for i in range(6):
    mask = 1 << i
    if switch_value & mask:
        print("Bit", i, "-", switch_names[i], "is ON")
    else:
        print("Bit", i, "-", switch_names[i], "is OFF")

