# climbing stairs:
def ways(stairs):
   #Base case 1
    if stairs < 0 :
        return 0
    # base case 2
    if stairs == 0:
        return 1
    # if stairs are more then 2 to take 2 stairs at a time 
    two = 0
    if stairs >= 2:
        two = ways(stairs-2)
    # one stair
    one = ways(stairs-1)
    # total distict path 
    return two+one
stairs = int(input("enter the number of stairs?"))
print("the number of distinct ways for ", stairs,"is :",ways(stairs))

# number of parentheses
def paren(s,l,r,p,n):
    #Base case 1
    if (p == 2*n):
        for ss in s :
            print(ss,end = " ")
        print("\n")
        return
    #Close - base brach
    if (l>r):
        s[p] = "}"
        paren(s,l,r+1,p+1,n)
    # Open - base branch
    if (l<n):
        s[p] = "{"
        paren(s,l+1,r,p+1,n)

n = int(input("enter the number of parentheses: "))
s = [""]* 2 * n
print("\n")
paren(s,0,0,0,n)
