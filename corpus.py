#! python3

import numpy as np 
import random

class Corpus():


	def __init__(self, filepath, order):

		self.filepath = filepath
		self.order = order


	def get_corpus(self):

		with open(self.filepath, "r") as text:

			corpus = text.read().replace('"', '').replace('”', '')

		return corpus


	def tokenize(self, corpus):
		
		_words = corpus.split()

		n_grams = []
		start_words = []
		end_words = []
		middle_words = []

		#step
		for i in range(0, (len(_words)-1), self.order):
	
			n_gram = ' '.join(_words[i: i + self.order])
			n_grams.append(n_gram)

		#same as: 
		#["-".join(words[i:i+span]) for i in range(0, len(words), span)]


		for w in n_grams:

			if w.istitle():
				start_words.append(w)

			elif w[-1] == '.':
				end_words.append(w)

			elif w[-1] == '?':
				end_words.append(w)

			else:
				middle_words.append(w)

		tokens = [start_words, end_words, middle_words, n_grams]

		return tokens
