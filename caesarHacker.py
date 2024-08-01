#Caesar Cipher Hacker-Brute Force
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = input("Enput your decrypted message!")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Look through every possible key
for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            translated_index = SYMBOLS.find(symbol)
            translated_index = translated_index - key

            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)

            translated = translated + SYMBOLS[translated_index]

        else:
            translated = translated + symbol
        
    key = str(key)        
    print(key+":"+translated+"\n") 
