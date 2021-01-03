def sieve_of_eratosthenes(num): 
    result = set()
    prime_labels = [True for i in range(num+1)] 
    pos = 2
    #search up to sqrt(n)
    while (pos**2 <= num): 
        if (prime_labels[pos] == True): 
            #if prime found, make multiples->false
            for i in range(pos * 2, num+1, pos): 
                prime_labels[i] = False
        pos += 1
    
    #once done store primes in Set
    for p in range(2, num):
        if prime_labels[p]: 
            result.add(p)
    
    return result 


#primes and squares for worst case
primes = sieve_of_eratosthenes(500000) #set for O(1) access
squares = [2 * x**2 for x in range(500)]

for _ in range(int(input())):
    #take number
    number = int(input())
    #ways it can be written as
    ways = 0
    for i in squares:
        #dont search too high on squares
        #cause this costs. its a 500 elem' list
        if i > number:
            break

        #solve equation num = prime + 2*square
        #==> prime = num-2*square
        #so if there is a prime we increase counter
        if (number - i) in primes:
            ways += 1
    
    #print total ways
    print(ways)
