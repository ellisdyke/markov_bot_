#! python3

import numpy as np 
import random

def probabilities(words):

	counts = {}
	w = len(words) - 1
	

	for i in range(w):

		if words[i] not in counts:
			counts[words[i]] = [words[i + 1]]

		else:
			counts[words[i]].append(words[i + 1])

	return counts