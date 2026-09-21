def sum_multiples(limit,n):
    count=0
    for i in range(1,limit):
        if i%n==0:
            count=count+i
        else:
            count=count+0
    return count
limit=int(input("enter a number for range \n"))
n=int(input("enter a number to divide \n"))
count= sum_multiples(limit,n)
print(count)