#! python3

import corpus
import parse_corpus
import markov

def generate(tokens, counts_, o):

	chain = markov.chain(tokens[0], tokens[1], tokens[2], counts_, o)
	
	print(*chain, sep=' ')
	print('\n')

	return chain


def init():

	filepath = '/home/hr/Scripts/python/markov_chains/elliot/test_corpus.txt'


	while True:

		r = input('\n[ENTER]: Continue [Q]: Quit \n').lower()

		if r == 'q':
			break

		else:

			order = int(input('Enter n-gram order:  '))
			num_sentences = 5

			c = corpus.Corpus(filepath, order)
			words = c.get_corpus()
			tokens = c.tokenize(words)
			counts = parse_corpus.probabilities(tokens[3])

			i = 0

			while i <= num_sentences:

				generate(tokens, counts, order)

				i += 1
			
		
	
init()