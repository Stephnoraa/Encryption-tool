import random
import string
from operator import index

#To create a list of characters
chars = string.punctuation + string.digits + string.ascii_letters
#Turns this character string into a list
chars = list(chars)
#Create a duplicate or a copy of the list
key = chars.copy()

random.shuffle(key)


#To Encrypt
plain_text = input("What message do you want to encrypt? Enter it here: ")
cipher_text =  ""

for i in plain_text:
    index= chars.index(i)
    cipher_text += key[index]

print(f"This is the original message: {plain_text}")
print(f"This is your encrypted message: {cipher_text}")

# To Decrypt
cipher_text = input("What message do you want to decrypt? Enter it here: ")
plain_text = ""

for i in cipher_text:
    index = key.index(i)
    plain_text += chars[index]

print(f"This is the encrypted message: {cipher_text}")
print(f"This is your decrypted message: {plain_text}")