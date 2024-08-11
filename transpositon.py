#Transposition Encrypt

import pyperclip
import array
import re

#main function
def main():
    #This message to be encrypted
    message = input("Input your plaintext\n")

    #The encrypted key
    key = input("Input your encrypted key, such as 8, not word\n")
    if re.search(r'\D',key):
        print("Your key is error!\n")
    else:
        output = generate_cipher(message,key)
        print("Your Cipher message is:"+output)

#Generate the cipher message
def generate_cipher(message,key):

    #setup the transposition matrix
    index = 0
    key = int(key)
    cols = key
    rows = 1
    summ = rows*cols

    #As the length of message is longer than summ, increasing the length of summ
    while len(message) > summ:
        rows += 1
        summ = rows*cols
        
    matrix = [[0]*cols for _ in range(rows)]

    #put the message into the matrix
    for i in range(rows):
        for j in range(cols):
            if index < len(message):
                matrix[i][j] = message[index]
                index += 1
            else:
                matrix[i][j] = ' '

    #Pick out the result of transposition cipher way
    output = ''
    for b in range(cols):
        for a in range(rows):
            restored_output = ''.join(matrix[a][b])
            output += restored_output
    return output

if __name__ == "__main__":
    main()
