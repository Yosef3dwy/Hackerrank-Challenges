def minion_game(string):
    # your code goes here
    
    vowels = "AEIOU"
    Kevin_score = 0
    Stuart_score = 0
    
    
    for i in range(0, len(string)):
        if string[i] in vowels:
            Kevin_score += len(string) - i
    
        elif string[i] not in vowels:
            Stuart_score += len(string) - i
    
    if Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    
    elif Stuart_score < Kevin_score:
        print(f"Kevin {Kevin_score}")
    
    elif Stuart_score == Kevin_score:
        print("Draw")