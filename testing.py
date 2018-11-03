from patterns import pattern_list

def agglutinator(list,pattern):

    print("Token list: ", list)

    if len(pattern) == 0 : return

    new_list, buffer = [], []
    
    i, j = 0, 0

    while (i < len(list)) :

        buffer.append(list[i])
        print("Buffer: ", buffer)

        if pattern == tuple(buffer) :
            print("Pattern found: ", pattern, " ==> ", pattern_list[pattern])
            new_list.append(pattern_list[pattern])
            buffer = []
            j = 0

        if len(buffer) != 0 and pattern[j] == buffer[j] :
            j = j + 1
        else :
            new_list.extend(buffer)
            buffer = []
            j = 0

        i = i + 1

    return new_list

list = ["VERB","AUX_VERB","AUX_VERB","NOMINAL", "OTHER"]
pattern = ("AUX_VERB","AUX_VERB")
pattern2 = ("VERB","AUX_VERB")

print(agglutinator(agglutinator(list,pattern),pattern2))
#print(agglutinator(list,pattern2))