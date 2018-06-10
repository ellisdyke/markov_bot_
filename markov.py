#! python3

import numpy as np 
import random


def chain(starts_, ends, mid, counts_, order):

    strt = random.choice(starts_)
    current_word = strt
    sentence = [current_word]
    #order = number of words per token
    #words per sent = number of tokens of said order to use
    words_per_sent = (random.randint(5, 15) / order)

    i = 0

    while i < (words_per_sent - order):
        
        next_word = random.choice(counts_.get(current_word))

        if next_word not in starts_ and next_word not in ends:

            sentence.append(next_word)
            current_word = next_word 
        
        i += order

    
    e = random.choice(ends)
    sentence.append(e)

    return sentence
