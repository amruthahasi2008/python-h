#Countdown
def countdown(n):
    if n == 0:
        print("Time's up!")
        return
    print(n)
    countdown(n - 1)
print("Countdown from 10")
countdown(10)

#countup
def countup(n):
    if n > 10:
        return
    print(n)
    countup(n + 1)
print("Counting  up from 1 to 10")
countup(1)

