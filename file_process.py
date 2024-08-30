# Encrypt/Decrpyt file by transposition way

import os
import transpositon
import transpositon_decrypt


def main():
    input_file = input("Input your file\n")

    if not os.path.exists(input_file):
        print('Your file does not exist!\n')
        sys.exit()
    else:
        input_choice = input('Input your way, encrypt or decrypt?\n')
        if input_choice == 'encrypt':
            input_key = input('Input your encrypted key, 1 to infinity.\n')
            input_key = int(input_key)
            encrypt_file(input_file,input_key)
        elif input_choice == 'decrypt':
            input_key = input('Input your decrypted key, 1 to infinity.\n')
            input_key = int(input_key)
            decrypt_file(input_file,input_key)
        else:
            print('Your input way is error!\n')
            sys.exit()

def encrypt_file(file,key):
    f = open(file,'r',encoding='utf-8')
    gett = f.read()
    encrypted = transpositon.generate_cipher(gett,key)
    f.close()

    f = open(file,'w',encoding='utf-8')
    f.write(encrypted)
    f.close()


def decrypt_file(file,key):
    f = open(file,'r',encoding='utf-8')
    gettt = f.read()
    decrypted = transpositon_decrypt.generate_plaintext(gettt,key)
    f.close()

    f = open(file,'w',encoding='utf-8')
    f.write(decrypted)
    f.close()    
    
        
    
if __name__ == '__main__':
    main()
