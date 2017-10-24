import RSA

public_key = (2539771189, 7)
private_key = (2539771189, 725620063)  

mess = 'testing testing 123 123456 hi dave'

ascii_mess = [ord(char) for char in mess]

print(ascii_mess)

encrypted_ascii_mess = [RSA.encrypt(public_key, message) for message in ascii_mess]

print(encrypted_ascii_mess)

decrypted_ascii_mess = [RSA.decrypt(private_key, message) for message in encrypted_ascii_mess]

print(decrypted_ascii_mess)

decrypted_mess = ''

for char in decrypted_ascii_mess:
    decrypted_mess += chr(char)

print(decrypted_mess)
print(mess)




