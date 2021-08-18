def rec_product(a, b):

    '''Calculate product a * b recursively'''

    if b == 0:
        return 0
    elif b > 0:
        return a + rec_product(a, b - 1)
    elif b < 0:
        return -a + rec_product(a, b + 1)

print (rec_product(8, -6))

#rec_product (4,3) 
#returns 4 + 4 + 4 + 0
#rec_product (4,2) -> returns 4 + 4 + 0
#rec_product (4,1) -> returns 4 + 0
#rec_product (4,0) -> returns 0 
#replace rec_product (4,0) 

#Recursions are repetition of tasks. In this example, there is repeated multiplication of a by B. The way this recursion is set up, if b is equal to zero then it is zero. This is our base case and the reason why the recursion breaks and does not keep going. Examplel 1 Situation 1: If we were to repplace rec_product (a,b) with re_product (4, 5) then it would return 4 + rec_product (4, 4). Rec_product would repeat itself again by returning 4 + rec_product (4, 3). On and on until b equals 0. After the break, the return 0 would replace the other returns (See example above).