if __name__ == '__main__':
    lst = []
    inp = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inp = [name, score]
        lst.append(inp)

    lst.sort(key = lambda x: (x[1], x[0]))
    Min = [0, lst[0][0], lst[0][1]]
    
    for i in range(0, len(lst)):
        if lst[0][1] < lst[i][1]:
            sec_min_idx = i
            break
    
    for j in range(i, len(lst)):
        if lst[sec_min_idx][1] == lst[j][1]:
            print(lst[j][0])