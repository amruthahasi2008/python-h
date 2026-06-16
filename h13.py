num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    lcm = num1
else:
    lcm = num2
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm = lcm + 1
print("LCM is:", lcm)