# Detect English word Module

import math

# Calculate the partion of english symbol or space in string 
def wordPartion(message, template):
    total_chars = len(message)

    sum_words = 0

    for c in message:
        if c in template:
            sum_words = sum_words + 1
        else:
            sum_words = sum_words

    word_partion = math.floor((sum_words/total_chars)*100)

    return word_partion
    
# Calculate the partion of english word in string
def englishPartion(message, ttemplate):

    # Load the dictionary data and transfer them to dictionary type
    dictionary_file = open('dictionary.txt')
    english_words = {}
    for words in dictionary_file.read().split('\n'):
        english_words[words] = None
    dictionary_file.close()

    # Remove the space symbol, ' \t\n' in message and transfer it to list type 
    letters_only = []
    for m in message:
        if m in ttemplate:
            letters_only.append(m)
    letters_only = ''.join(letters_only)    
    letters = letters_only.split()

    # Judge the partion for english words in string
    len_letters = len(letters)
    sum_english_words = 0

    for l in letters:
        l = l.upper()
        if l in english_words:
            sum_english_words = sum_english_words +1
        else:
            sum_english_words = sum_english_words

    english_word_partion = math.floor((sum_english_words/len_letters)*100)

    return english_word_partion


def is_English(message,wordPercentage,englishPercentage):

    testing = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stesting = testing + testing.lower() + ' \t\n' 

    if message == '':
        return 'n'
    else:
        res1 = wordPartion(message, stesting)
        if res1 >= wordPercentage:
           res2 = englishPartion(message,stesting)
           if res2 >= englishPercentage:
               return 'y'
           else:
               return 'n'
        else:
            return 'n'

    

    
