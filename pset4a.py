def get_permutations(sequence):
    if len(sequence) == 1:   #If there's just 1 character, then there are no combinations to give.
        return list(sequence)

    final_list = []
    l = get_permutations(sequence[1:])     #Runs recursively
    s = l[:]                               #Need to duplicate l. For some reason if I don't do this, the code runs infinitely. Probably has to do with how lists reference each other.
    for terms in s:                        #The way the code runs is we take all the combinations of the sequence minus the first character, then we add that character to all positions in all combinations
        for i in range(0, len(terms) + 1): #This loop is run for the length of the term, as the character will be inputed into that many positions in the term
            lst = list(terms)              #We take the first term, and turn it into a list of its characters. E.g. 'abc' --> ['a', 'b', 'c']
            lst.insert(i, sequence[0])     #Insert the new character into the ith position in the list.
            list_to_string = ''.join(lst)  #Turn the list into a string
            final_list.append(list_to_string)
    return sorted(final_list) 

characters = input("")
print(get_permutations(characters))
