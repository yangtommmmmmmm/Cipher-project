#Transposition Auto Test

#import module，such as random、sys、transpositon.py and transpositon_decrypt.py
#You could also rewrite the follow statements: import random, sys, transpositon,transpositon_decrypt
import random
import sys
import transpositon
import transpositon_decrypt


def main():
    #Set the function for generating pseudo random numbers 
    random.seed(42)

    # Test for 20
    for i in range(20):
        # multiples for ABCDEFGHIJKLMNOPQRSTUVWXYZ
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*random.randint(4,40)
        # transfer the message from string to list
        message = list(message)
        # shuffle the list
        random.shuffle(message)
        # transfer the list from list to string
        message = ''.join(message)

        print('Test #%s: "%s..."'%(i+1, message[:50]))

        for key in range(1,int(len(message)/2)):
            # Call the generate_cipher function in transpositon.py to generate the cipher text.
            encrypted = transpositon.generate_cipher(message, key)
            # Call the generate_plaintext function in transpositon_decrypt to decrypt the cipher text to plaintext.
            decrypted = transpositon_decrypt.generate_plaintext(encrypted,key)


            # if original message is as same as plaintext, continue; no same, go sys.exit() and show that
            # your transposition algorithm has some error.            
            if message != decrypted.rstrip(): # rstrip function is for deleting the space located on the tail of
                                              # string.
                print('Mismatch with key %s and message %s.'%(key,message))
                print('Decrypted as:' + decrypted)
                sys.exit()

    print('Transposition cipher test passed!')

if __name__ == '__main__':
    main()



