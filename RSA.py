import random
import math

class RSA():
    
    def __init__(self, q=0, p=0):
        '''
        Builds values and calculates elements used in the encryption
        and decryption process.
        '''
        if p == 0 and q == 0:
            p = int(self.lazy_primes()[0])
            q = int(self.lazy_primes()[1])
        
        # Checks the primes are different, if not re-chooses them.
        while p == q:
            p = int(self.lazy_primes()[0])
            q = int(self.lazy_primes()[1])            
        
        n = p * q
        phi_n = (p - 1) * (q - 1)
        
        # Finds e so that it is not a divisor of p or q.        
        for e in range(3, phi_n, 2):
            if self.are_prime(e, phi_n):
                break
        
        # Finds d
        d = self.modinv(e, phi_n)
        
        public_key = (n,e)
        private_key = (n,d)
        
        self.p = p
        self.q = q
        self.n = n
        self.d = d
        self.phi_n = phi_n
        self.e = e
        self.private_key = private_key
        self.public_key = public_key 
        
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)
        
    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        return x % m
    
    def are_prime(self, a, b):
        """
        Return True if a and b are two relatively prime numbers.
        """
        
        for n in range(2, min(a, b) + 1):
            if a % n == b % n == 0:
                return False
        return True  
        
    def lazy_primes(self):
        '''
        Returns two primes randomly chosen from list "primes.txt"
        '''
        
        file = open('primes.txt')
        primes = file.readlines()
        
        counter = 0
        for i in primes:
            primes[counter] = i[:-1]
            counter += 1
            
        first_prime = primes[random.randint(0,len(primes))]
        second_prime = primes[random.randint(0,len(primes))]
        
        return first_prime, second_prime
    
        
    def __str__(self):
        '''
        Prints readout of p, q, n, phi_n and the public key.
        '''
        
        readout = 'p = ' + str(self.p) + \
            '\n' + 'q = ' + str(self.q) + \
            '\n' + 'n = ' + str(self.n) + \
            '\n' + 'φ(n) = ' + str(self.phi_n) + \
            '\n' + 'Public Key = ' + str(self.public_key) + \
            '\n' + 'Private Key = ' + str(self.private_key)
            
        return readout


def encrypt(public_key, message):
    '''
    Encrypts ciphertext, with public key.
    '''    
    
    e = public_key[1]
    n = public_key[0]    
    
    cipher_text = ''
    
    for char in message:
        if char != ' ':
            char = char.lower()
            num = ord(char) - ord('a') + 1
            num = (num ** e) % n
            
            #cipher_text += str(chr(num + ord('a') - 1))
            
            cipher_text += str(num)
            cipher_text += ' '
            
        else:
            cipher_text += ' '
    
    return cipher_text
        
        


    
def decrypt(private_key, cipher_text):
    '''
    Decrypts ciphertext, with private key.
    '''
    
    d = private_key[1]
    n = private_key[0]    

    encrypted_ascii_mess = cipher_text.split(' ')

    decrypted_mess = ''
    
    for char in encrypted_ascii_mess:
        decrypted_mess += chr(pow(int(char), d, n))

    return decrypted_mess

#cipher = RSA()
#print(cipher)

message = input()


test = encrypt((2183, 97), message)
print(test)
#print(decrypt((2463427013, 1407614263), test))


