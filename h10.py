num = int(input("Enter a number: "))
binary = 0
while num > 0:
    digit = num % 10                
    binary = (binary * 10) + digit  
    num = num // 10  

print("Reversed number:", binary)
l = []
for i in str(binary) :
    l.append(int(i)*(2**l[int(i)]))
    b = sum(l)
 
    