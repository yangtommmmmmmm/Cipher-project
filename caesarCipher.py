#Caesar Cipher
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)


import pyperclip

#This message to be encrypted/decrypted
message = input('Enter your plaintext\n')

#The encrypted/decrypted key
key = input('Enter your key length, such as 15\n')
key = int(key)

#Whether the program encrypts or decrypts
mode = input('Enter your method-\'encrypt\' or \'decrypt\'\n')

#Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Store the encrypted/decrypted form of the message
translated = ''


for symbol in message:
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)

        #Perform encryption/decryption:
        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key


        #Handle wraparound
        if translated_index >= len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)

        translated = translated + SYMBOLS[translated_index]

    else:
        #Append the symbol without encrypting/decrypting
        translated = translated + symbol


print(translated)
pyperclip.copy(translated)


        
