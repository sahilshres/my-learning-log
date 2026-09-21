def prime(n):
    count=0
    for i in range(2,n):
        is_prime=True
        for j in range(2,i):
            if n%i==0:
             is_prime= False
        if is_prime==True:
            count=count+1
    return count
n=int(input("enter a number \n"))
e= prime(n)
print(e)