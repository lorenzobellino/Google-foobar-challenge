#the problem can be described as finding the
#distinct partitions of a given number
#that means all the possibilities in which that number
#can be represented as a sum of k number different from each other
#for examples:
# p(5) = partitions of 5:
# (5)=(4+1)=(3+2)=(3+1+1)=(2+1+1+1)=(1+1+1+1+1)
#pD(5) = distinct partition of 5:
# (5)=(4,1)=(3,2)
#the total number of different arrangements of the number n
#can be expressed as the coefficient of the variables x^n
#derived from the Euler's partitions formula:
#(1+x)*(1+x^2)*(1+x^3).....(1+x^n)
#if we display the formula we obtain:
#1+x+x^2+2x^3+2x^4+3x^5+4x^6...
#as we can see this formula consider also the partition pD(5)=5
#so we have to subtract 1 from the final result in order to abtain the correct answer

#in order to solve the problem i created 2 lists of lenght n+1
#and fill them with zeroes exept for the first two elements that are 1 and 1
#ecouse the first terms of the sequences is (1+x) which coefficients are 1 and 1


def adding_new_coefficients ( a, b, n):

#this function is meant to transfer the partial result from the list savings
#to the final list of result distinct_partitions
    for q in range (2,n+1):
        b[q]=  a[q]
    return b

def answer(n):
    distinct_partitions=[]
    savings=[]
    new_range = 2
    
#create the two lists:
#distinct_partition scores the final result
#savings score the partial result

    for f in range (n+1):
        distinct_partitions.append(0)
        savings.append(0)
    distinct_partitions[0]=1
    distinct_partitions[1]=1
    savings[0]=1
    savings[1]=1

#in this two cicles i represent the exponent of the next term to multiply to the sequence
#it starts at 2 becouse the first new terms is (1+x^2) and increments untill it reaches n

#j represent the exponent of the terms that has to be multiplied
#and it starts at 0 and increments untill the coefficient of the next terms is 0
#this information is stored in k and new_range


    for i in range (2,n+1):
        k = new_range
        for j in range (k+1):

            if i+j <= n:
                savings[i+j] += distinct_partitions[j]

            new_range = i+j

#in the and i and j are the exponent of the terms and the index of the lists
#but the but the elements stored at a given index 'a' are the coefficientse
#of the variables x^a

#finally i use a function to transfer the partial result stored in the list savings
#and copy the result to the final lis
        
        distinct_partitions=adding_new_coefficients(savings,distinct_partitions,n)
        
    
#as i mentioned before the final result is the element stored in distinct_partitions
#in the position n
#subtracted by one
    number_of_stairs=distinct_partitions[n]-1
    return number_of_stairs


if __name__ == "__main__":

    print(answer(705))
