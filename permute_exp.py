def permute2(seq):
    if not seq:  # Shuffle any sequence: generator
        yield seq  # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Delete current node
            for x in permute2(rest):  # Permute the others
                yield seq[i:i + 1] + x

def fourexp7(L):
    if not L:
        yield L
    else:
        for x in range(4):
            for y in fourexp7(L[1:]):
                yield [x]+y

x=[1,1,1]  
y=[1,2,3]
M=len(list(fourexp7(x)))
print (M)
