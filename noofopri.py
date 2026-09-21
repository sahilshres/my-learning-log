def prime(n):
    count=0
    pcount=0
    for i in range(2,n+1):
        pcount=0
        for j in range(2,i+1):
            if i%j==0:
                pcount=pcount+1
            else:
                pcount=pcount
        if pcount==1:
            print(i)
        else:
            continue
    return count
n=int(input("enter a number \n"))
e= prime(n)