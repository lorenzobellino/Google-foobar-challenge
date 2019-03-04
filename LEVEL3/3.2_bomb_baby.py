def answer(M,F):
    generations = 0
    a = int(M)
    b = int(F)

    if a < b:
        c = a
        a = b
        b = c
        
    while b >= 1:
        d = a // b
        e = a % b
        generations += d
        a = b
        b = e

    if a != 1:
        return "impossible"
    else:
        return str(generations-1)


