# -*- coding: utf-8 -*-

def compare_first_letter(phrase, compare_letter):
    '''
        Esta função serve para comparar uma letra (compare_letter) com as primeiras 
        letras de cada palavra de uma frase(phrase). Se a letra for igual às primeiras letras, ela retorna True,
        senão ela retorna False.
    '''
    # making all unicode objects, with utf-8 codec
    compare_letter = unicode(compare_letter, encoding='utf-8')
    phrase = unicode(phrase, encoding='utf-8')
    # taking the first letters of each word in phrase
    first_letters = [word[0] for word in phrase.split()]
    # comparing the  first letters with the letter you want
    for letter in first_letters:
        if letter != compare_letter:
            return False
    return True  # or your reply function

letter = 'ç'
phrase_1 = "one two three four"
phrase_2 = "çarinha çapoca çamuca"

print(compare_first_letter(phrase_1, letter))
print(compare_first_letter(phrase_2, letter))
