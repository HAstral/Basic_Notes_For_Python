import random
import string



chars = " " + string.punctuation + string.ascii_letters + string.digits
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)
# print(f"chars: {chars}")
# print(f"keys: {keys}")
#6:00:49
# print(help(random))
#encrypt
plain_text=input("Enter a message to encrypt: ")
ciper_text=" "

for letter in plain_text:
    index=chars.index(letter)
    ciper_text+=keys[index]

print(f"original message is  : {plain_text}")
print(f"encrypted message is : {ciper_text}")

#decrypt
ciper_text=input("Enter a message to encrypt: ")
plain_text=" "

for letter in ciper_text:
    index=keys.index(letter)
    plain_text+=chars[index]

print(f"encrypted message is : {ciper_text}")
print(f"original message is  : {plain_text}")
