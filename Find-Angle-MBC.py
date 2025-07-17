# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input().strip())
BC = int(input().strip())

degree = round(math.atan(AB/BC) * (180 / math.pi))

print(f"{int(degree)}\u00b0")
