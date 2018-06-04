#! python3

import numpy as np 
import random


c = "I am a little tea pot short and stout short and cute a little pot I am"


#works 
def get_corpus():

	start_words = []
	end_words = []
	middle_words = []
	all_words = []

	r = input('[ENTER]: Continue [Q]: Quit').lower()

	if r != 'q':

		#filepath = input('\n\nEnter file path:  ')
		filepath = '/home/hr/Scripts/python/markov_chains/test_corpus.txt'

		with open(filepath, "r") as text:

			corpus = text.read().replace('"', '').replace('”', '')

		_words = corpus.split()

	for w in _words:

		if w.istitle():
			start_words.append(w)

		elif w[-1] == '.':
			end_words.append(w)

		elif w[-1] == '?':
			end_words.append(w)

		else:
			middle_words.append(w)

	c = [start_words, end_words, middle_words, _words]

	return c


#works
def parse_corpus(words):

	counts = {}
	w = len(words) - 1
	

	for i in range(w):
			
		if words[i] not in counts:
			counts[words[i]] = [words[i + 1]]

		else:
			counts[words[i]].append(words[i + 1])

	return counts 


#works!!
def generate_sentence(starts_, ends, mid, counts_):

	strt = random.choice(starts_)
	current_word = strt
	sentence = [current_word]
	n = 10
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

	
		
def init():

	wl = get_corpus()
	starts = wl[0]
	ends = wl[1]
	mid = wl[2]
	allwords = wl[3]
	counts_list = parse_corpus(allwords)

	markov = []

	size = int(input('\nEnter # of sentences to generate: ').lower())
	i = 0

	while i != size:

		s = generate_sentence(starts, ends, mid, counts_list)
		markov.append(s)
		i += 1


	for chain in markov:
		print('\n\n', *chain, sep=' ')

init()
