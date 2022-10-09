def get_permutations(sequence):
    if len(sequence) == 1:
        return list(sequence)

    k = []
    l = get_permutations(sequence[1:])
    s = l[:]
    for terms in s:
        for i in range(0, len(terms) + 1):
            lst = list(terms)
            lst.insert(i, sequence[0])
            y = ''.join(lst)
            k.append(y)
    return sorted(k)

print(get_permutations('abc'))
