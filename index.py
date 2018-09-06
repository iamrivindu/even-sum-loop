def sumOfEs(I):
    L=[]
    sum = 0
    for i in I:
        L.append(i)
    if (1<int(I)<10**5):
        for J in L:
            if(int(J)%2 == 0):
                sum=sum+int(J)
        print (sum)
        return sum
    else:
        print("Please enter string with digits in range")
                
def addMember(K):
    if (K>=10):
        sum =0
        L=[]
        for i in str(K):
            L.append(i)
        for j in L:
            sum=sum+int(j)
        print (sum)
        if (sum>10):
            addMember(sum)
        
addMember(sumOfEs("4765"))
