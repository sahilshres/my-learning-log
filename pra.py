def count_primes(limit):
    count = 0                          
    for n in range(2, limit):         
        is_prime = True                
        for i in range(2, n):         
            if n % i == 0:             
                is_prime = False      
        if is_prime:                   
            count = count + 1         
    return count
limit = int(input("Enter a number\n"))
result = count_primes(limit)
print(result)