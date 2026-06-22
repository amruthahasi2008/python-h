#Part 1
n = int(input("Enter the number"))
temp = n
while temp>0:
    print("The last digit :",temp%10,"Remaining digits:",temp//10)
    temp = temp//10
print()

# Part 2
def reversedn(n, rev = 0):
    if n //10 == 0:
        return n
    else:
        last = n % 10
        rev = rev * 10 + last
        rest = reversedn(n//10)
n2 = int(input("Enter the number you want to reverse"))
print("The reversed number is :",reversedn(n2))

#Part 3
def flipname(s):
    if len(s) == 1:
        return s
    else:
        return flipname(s[1:])+s[0]
    
name = input('Enter the name')
print("the flipped name is ",flipname(name))

#Part 4
def isPower4(n):
    if n <= 0:
        return False
    if n == 1 :
        return True
    if n % 4 == 0:
        return isPower4(n//4)
    return False
guess = int(input("test your own number"))
print(guess,"power of 4 ->",isPower4(guess))
    