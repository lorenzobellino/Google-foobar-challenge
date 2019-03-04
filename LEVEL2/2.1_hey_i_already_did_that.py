def from_decimal_to_base (dec_n , b):
    digits=[]
    quoto=0
    m=0
    while dec_n>=b:
        quoto = int(dec_n % b)
        dec_n = int((dec_n - quoto)/b)
        digits.append(quoto)
        m=m+1
    digits.append(dec_n)
    result = digits[::-1]
    conv ="".join(str(x) for x in digits)
    conv = int(conv)
    return conv

def from_base_to_decimal (n_base , current_base , k):
    string_n = str(n_base)
    n_dec=0
    for i in range (0,k):
        n_dec= n_dec + (int(string_n[k-i-1])  * (current_base ** i))

    n_dec = int (n_dec)
    return n_dec

  


def subtract(x,y,b,k):
    
    if b==10:
        return int(x)-int(y)
    else:
        decimal_x = from_base_to_decimal (x , b , k)
        decimal_y = from_base_to_decimal (y , b , k)
        decimal_z = decimal_x - decimal_y
    base_b_z = from_decimal_to_base (decimal_z , b)
    base_b_z = int (base_b_z)
    return base_b_z
                          
def answer(n,b):
    
    k = len(str(n))
    array=[]
    number="".join(sorted(str(n), reverse= True))
    number=int(number)
    array.append(number)
    print (array)
    trovato=0
    while  trovato==0:
        x="".join(sorted(str(n), reverse=True))
        y="".join(sorted(str(n)))

        z=subtract(x,y,b,k)

        lenght_z = len(str(z))
        lenght_x = len(str(x))
        lenght_y = len(str(y))

        if lenght_z != lenght_x:
            z = z * pow(10, (lenght_x-lenght_z))

        actual=str(z)
        actual="".join(sorted(str(actual), reverse = True))
        actual=int(actual)

        array.append(actual)
        lenght= len(array)

        print (actual)

        print(array)
        print (lenght)

        for j in range (0, lenght-1):
            print (j)
            if array[j]==actual:
                trovato=1
                index=lenght-1-j
        n=int(z)


    return index

    
    

