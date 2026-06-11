# MY RUNNING LAP TRACKER
# Topics:
# Algorithm | Pseudocode | Time Complexity | Space Complexity
# One Problem, Three Solutions | Comparing Algorithm Efficiency

# Problem:
# A runner completes laps.
# Lap 1 = 1 point, Lap 2 = 2 points, Lap 3 = 3 points, and so on.
# Find the total running points after n laps using three different solutions.

n = 5
print("MY RUNNING LAP TRACKER")
print("Number of laps:", n)
print()

# SOLUTION 1 - FORMULA METHOD
# Algorithm:
# Use the formula n * (n + 1) / 2 to calculate total points directly.
# Pseudocode:
# START
#   total = n * (n + 1) / 2
#   print total
# END
# Time Complexity: O(1)
# Space Complexity: O(1)

for_tot = n * (n + 1) // 2

print("Solution 1")
print("Total Points:", for_tot)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()

# SOLUTION 2 - LOOP METHOD
# Algorithm:
# Start from 0.
# Add each lap number one by one.
# total = 0
# FOR lap FROM 1 TO n
# total = total + lap
# print total
# Time Complexity: O(n)
# Space Complexity: O(1)

loop_t = 0
steps = 0

for i in range(1, n + 1):
    loop_t = loop_t + i
    steps = steps + 1

print("Solution 2:")
print("Total Points:", loop_t)
print("Steps:", steps)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()

# SOLUTION 3 - NESTED LOOP METHOD
# Algorithm:
# For each lap, count points one by one using another loop.
#total = 0
#FOR lap FROM 1 TO n
# FOR point FROM 1 TO lap
#total = total + 1
# print total
# Time Complexity: O(n^2)
# Space Complexity: O(1)

nested = 0
steps_n = 0

for i in range(1, n + 1):
    for point in range(1, i+ 1):
        nested = nested + 1
        steps_n = steps_n + 1

print("Solution 3:")
print("Total Points:", nested)
print("Steps Taken:", steps_n)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()
