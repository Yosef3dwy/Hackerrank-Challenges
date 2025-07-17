def merge_the_tools(string, k):
    # your code goes here
    k_counter = 0
    t_string = ""
    u_string = ""
    
    for i in range(0, len(string)):
        k_counter = i % k
    
        if k_counter == k - 1:
            t_string = string[i - k + 1: i + 1]
            u_string = ""
    
            for j in range(0, k):
                if t_string[j] not in u_string:
                    u_string += t_string[j]
    
            print(u_string)
