#Reverse Cipher
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)


plaintext = input('Enter your plaintext:')
ciphertext = ''

i = len(plaintext)-1
while i >=0:
    ciphertext = ciphertext+plaintext[i]
    i = i-1

print('Your ciphertext is:'+ciphertext)

