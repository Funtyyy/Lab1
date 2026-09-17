def minimal(ll):
    min1 = ll[0]
    for i in ll:
        if i < min1:
            min1 = i
    print(min1)


num = [1, 5, 6,2 ,4 , 4, 4321, 6]
minimal(num)    
        