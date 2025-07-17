def print_rangoli(size):
    alph = "abcdefghijklmnopqrstuvwxyz"
    center = size*2 - 2
    char_index = size - 1
    char_pos = 0
    out = ""
    
    for i in range(0, center + 1):
        for j in range(0, center*2 + 1):
            if (j % 2 == 0) and ((j >= center - (2 * char_pos)) and (j <= center + (2 * char_pos))):

                out += str(alph[char_index])

                if j >= center:  
                    char_index += 1

                elif j < center:
                    char_index -= 1

            else:
                out += "-"

        if i >= size - 1:
            char_pos -= 1

        elif i < size - 1:
            char_pos += 1

        char_index = size - 1
        out = out + "\n"

    print(out)