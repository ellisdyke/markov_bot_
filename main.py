#! python3

import corpus
import parse_corpus
import markov_

def debug(tokens, counts):
	start = tokens[0]
	end = tokens[1]
	mid = tokens[2]

	i = 0
	m = 5

	while i <= m:
		for item in counts:
			print('KEY: ', item, 'VAL: ', counts[item])

		i += 1

def generate(tokens, counts_):

	
	

	
	chain = markov_.chain(tokens[0], tokens[1], tokens[2], counts_)
	return chain

def init():

	filepath = '/home/hr/Scripts/python/markov_chains/test_corpus.txt'

	r = input('\n[ENTER]: Continue [Q]: Quit').lower()

	while r != 'q':

		#filepath = input('\n\nEnter file path:  ')
		
		order = int(input('Enter n-gram order:  '))
		#length = int(input('Enter # of sentences to generate:  '))
		length = 5

		c = corpus.Corpus(filepath, order)
		words = c.get_corpus()
		tokens = c.tokenize(words)
		counts = parse_corpus.probabilities(tokens[3])

		i = 0
		while i <= length:
			s = generate(tokens, counts)
			print(*s, sep=' ')
			print('\n')
			i += 1
		#debug(tokens, counts)
	
init()