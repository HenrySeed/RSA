from random import randint
from time import perf_counter

def is_prime(number):
    found = True
    
    if (number % 2) == 0:
        found = False
        
    for i in range(3, number, 2):
        if (number % i) == 0:
            found = False 
            
    return found

def prime_finder_fancy(current=randint(10000, 10000000)):
    
    start_time = perf_counter()
    print('Searching for primes, starting at: ' + str(current))
    
    if (current % 2) == 0:
        current += 1
        
    found = False
    
    while found == False:
        found = is_prime(current)
        if found == True:
            print('Sucess: ' + str(current))
            time_taken = (perf_counter() - start_time)
            print('Found in ' + ("%.2f" % time_taken) + 's')
        else:
            print('Failed: ' + str(current))
        current += 2  
        
        
        
def prime_finder(current=randint(10000, 100000000)):
    
    if (current % 2) == 0:
        current += 1
        
    found = False
    
    while found == False:
        found = is_prime(current)
        current += 2  
        
        
    if found == True:
        return current
    
    else:
        print('no prime found')

        
             
                
prime_finder_fancy()
print(prime_finder())