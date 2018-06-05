#! python3 

import numpy as np 
import random

def chain(starts_, ends, mid, counts_):

	strt = random.choice(starts_)
	current_word = strt
	sentence = [current_word]
	n = random.randint(5, 15)
	i = 0

	while i != n - 1:
		
		next_word = random.choice(counts_.get(current_word))

		if next_word not in starts_ and next_word not in ends:

			sentence.append(next_word)
			current_word = next_word 
		
		i += 1

	
	e = random.choice(ends)
	sentence.append(e)

	return sentence