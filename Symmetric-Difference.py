# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
set_N = set(list(map(int, input().split())))

M = int(input())
set_M = set(list(map(int, input().split())))

result = list(set_N ^ set_M)
result.sort()
for i in result:
    print(i)
