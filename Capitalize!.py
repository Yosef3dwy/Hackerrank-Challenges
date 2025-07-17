# Complete the solve function below.
def solve(s):
    alph_small = "abcdefghijklmnopqrstuvwxyz"
    alph_capit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    search_flag = 0
    
    for i in range(0, len(s)):
        if i == 0:
            search_flag = 1
        
        if s[i] == " ":
            if s[i + 1] == " ":
                continue
            
            elif s[i + 1] != " ":
                i += 1
                search_flag = 1
        
        if search_flag == True:
            for j in range(0, len(alph_small)):
                if s[i] == alph_small[j]:
                    s = s[0:i] + str(alph_capit[j]) + s[i + 1:]
                    break
                    
            search_flag = 0
         
            
    return s