if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    Max = -101

    arr.sort(reverse = True)
    Max = arr[0]
    runner_up = 0
    
    for i in arr:
        if Max > i:
            runner_up = i
            break
    
    print(runner_up)