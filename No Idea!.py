# Enter your code here. Read input from STDIN. Print output to STDOUT
(n, m) = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

count = 0

for x in arr:
    if x in set_A:
        count += 1
    
    if x in set_B:
        count -= 1

print(count)