def permute2(seq):
    if not seq:  # Shuffle any sequence: generator
        yield seq  # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Delete current node
            for x in permute2(rest):  # Permute the others
                yield seq[i:i + 1] + x

def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))                
                
def fourexp7(L):
    if L==0:
        yield []
    else:
        for x in range(4):
            for y in fourexp7(L-1):
                yield [x]+y

M=list(fourexp7(3))

print (M)
