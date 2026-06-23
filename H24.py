print("STACK FRAME VISUALIZER")
# LINEAR RECURSION
def linear_rec(n):
    if n == 0:
        return
    print("Linear call at level:", n)
    linear_rec(n - 1)
print("Linear Recursion")
linear_rec(5)

# PART 2
def tail(n):
    if n == 0:
        return
    print("tail",n)
    tail(n - 1)   
print("Tail Recursion")
tail(5)

# HEAD RECURSION
def head(n):
    if n == 0:
        return
    head(n - 1)
    print("head",n)
print("Head Recursion")
head(5)

#INCREASING DECREASING RECURSION
def inc_dec(n):
    if n == 0:
        return
    print("Going down ", n)
    inc_dec(n - 1)
    print("Coming up ", n)
print("Increasing-Decreasing Recursion")
inc_dec(5)

# TREE RECURSION
def tree_recursion(n):
    if n == 0:
        return
    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)
print("Tree Recursion")
tree_recursion(3)
