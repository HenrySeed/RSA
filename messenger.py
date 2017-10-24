import RSA

def messenger():
    cipher = RSA.RSA()
    
    quit = False
    print(cipher.public_key)
    while quit == False:
        message = input('> ')
        if message == 'quit':
            quit = True
            
        ciphertext = RSA.encrypt(cipher.public_key, message)
        
        print(ciphertext)
        
messenger()

#(1118137807, 11)