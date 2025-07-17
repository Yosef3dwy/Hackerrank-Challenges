lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
flag = 0

def swap_case(s):
    for i in range(len(s)):
        flag = 0
        chk_l = lowers.find(s[i]) 
        if chk_l != -1:
            s = s[:i] + uppers[chk_l] + s[i + 1:]
            flag = 1
            
        chk_u = uppers.find(s[i]) 
        if (chk_u != -1) and (flag == 0):
            s = s[:i] + lowers[chk_u] + s[i + 1:]
    return s

