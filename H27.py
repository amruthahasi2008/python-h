keypad = {
    "2":['a','b','c'],
    "3":['d','e','f'],
    "4":['g','h','i'],
    "5":['j','k','l'],
    "6":['m','n','o'],
    "7":['p','q','r','s'],
    "8":['t','u','v'],
    "9":['w','x','y','z']
}

def word(digits,current):
    if len(digits) == 0:
        print(current)
        return
    
    first_digit = digits[0]
    remaining = digits[1:]

    for l in keypad[first_digit]:
        word(remaining,current+l)

num = input ("enter the number")
print("All words:")
word(num,"")
