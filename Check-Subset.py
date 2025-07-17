# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    
    A = int(input())
    set_A = set(map(int, input().split()))
    B = int(input())
    set_B = set(map(int, input().split()))

    print(True) if (len(set_A - (set_B - (set_B - set_A))) == 0) else print(False)
