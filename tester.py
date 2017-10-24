import random

def lazy_primes():
    file = open('primes.txt')
    primes = file.readlines()
    
    counter = 0
    for i in primes:
        primes[counter] = i[:-1]
        counter += 1
        
    first_prime = primes[random.randint(0,len(primes))]
    second_prime = primes[random.randint(0,len(primes))]
    
    return first_prime, second_prime
    
    
    
def are_relatively_prime(a, b):
    """Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.

    Two numbers are relatively prime if they share no common factors,
    i.e. there is no integer (except 1) that divides both.
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def main():
    '''finds num where gcd(num, phi(n)) = 1'''
    p = 39097
    q = 39383
    n = 1539757151
    phi_n = 1539678672
    
    e = 5
    
    d = 1
    counter = 1
    while d == 1:
        if ((counter * e) % 1539678672) == 0:
            d = counter
            break
        else:
            counter += 1
    
    print(d)
main()
    