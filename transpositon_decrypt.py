#Transposition Descrypt

import pyperclip
import array
import re
import itertools
import math

#main function
def main():
    #This message to be decrypted
    message = input("Input your ciphertext\n")

    #Try any key to crack the cipher text，key from 1 to infinity
    for i in itertools.count(start=1):
        generate_plaintext(message,i)

#Generate the plaintext
def generate_plaintext(message,i):

    #Start with setting up the decrypted matrix
    index = 0
    part = len(message) / i
    part = int(part)
    part = math.ceil(part)
    
    cols = part
    rows = i

    matrix = [[0]*cols for _ in range(rows)]

           
    #put the cipher text into the matrix
    for a in range(rows):
        for b in range(cols):
            if index < len(message):
                matrix[a][b] = message[index]
                index += 1
            else:
                matrix[a][b] = ''


    #output the result of cracking, including key and plaintext
    output = ''

    for d in range(cols):
        for c in range(rows):
            restored_output = ''.join(matrix[c][d])
            output += restored_output
   
    i = str(i)       
    #print("Your key is:" + i +"\n")
    #print("Your plaintext is:" + output +"\n") 
    return output
    

    
if __name__ == "__main__":
    main()

    
