if __name__ == '__main__':
    N = int(input())
    inp = []
    num = 0
    idx = 0
    lst = []
    
    for i in range(0, N):
        inp = input().strip().split()
        
        if inp[0] == "insert":
            idx = inp[1]
            num = inp[2]
            
            lst.insert(int(idx), int(num))
            
        elif inp[0] == "append":
            idx = inp[1]
            
            lst.append(int(idx))
            
        elif inp[0] == "remove":
            idx = inp[1]
            
            lst.remove(int(idx))
            
        elif inp[0] == "print":
            print(lst)
            
        elif inp[0] == "sort":
            lst.sort()
            
        elif inp[0] == "reverse":
            lst.reverse()
            
        elif inp[0] == "pop":
            lst.pop()