def unique_in_order(sequence):
    li = list(sequence)
    i = 0
    while i < len(li):
        print(i, " a")
        if i+1 != len(li):
            while i+1 != len(li) and li[i] == li[i+1] :
                print(i, " b")
                if li[i] == li[i+1] : li.pop(i+1)
        i += 1        
    return(li)