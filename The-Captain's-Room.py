K = int(input())
lst = input().split()
counts = dict()

for i in lst:
    if i not in counts:
        counts[i] = 1
    
    else:
        counts[i] += 1

for x in counts:
    if counts[x] % K != 0:
        print(x)
        break
