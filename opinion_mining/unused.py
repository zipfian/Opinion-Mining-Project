#!/usr/bin/env python

"""
File that includes various features that have not yet been 
integrated into the main system, but will likely be of use later. 
"""

from __future__ import division
import re
import csv
from nltk.corpus import stopwords


class TokenProcessor():
	"""
	Class to handle all of the preprocessing steps on 
	a tokenized document. 
	"""

	# Make NLTK's stopwords list more sentiment-aware
	DELETE = {'should', 'don', 'again', 'not'}
	STOPWORDS = set(stopwords.words('english')).difference(DELETE)

	def __init__(self):
		pass

	def lower_case(self, tokens):
		"""Convert to lower case"""
		return [t.lower() for t in tokens]

	def filter_stop_words(self, tokens):
		"""Remove stop words"""
		return [t for t in tokens if t not in self.STOPWORDS]

class LiuFeaturizer():
	"""
	Class for scoring sentences using Bing Liu's Opinion Lexicon. 

	Source:

	Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA,

    Download lexicon at: http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar
	"""

	PATH_TO_LEXICONS = "/Users/jeff/Zipfian/opinion-mining/data/Lexicons"

	def __init__(self):
		"""
		Read in the lexicons. 
		"""

		pos_path = self.PATH_TO_LEXICONS + "/Liu/positive-words.txt"
		neg_path = self.PATH_TO_LEXICONS + "/Liu/negative-words.txt"

		self.pos_lex = self.read_lexicon(pos_path)
		self.neg_lex = self.read_lexicon(neg_path)


	def read_lexicon(self, path):
		'''
		INPUT: LiuFeaturizer, string (path)
		OUTPUT: set of strings

		Takes path to Liu lexicon and 
		returns set containing the full 
		content of the lexicon. 
		'''

		start_read = False
		lexicon = set() # set for quick look-up

		with open(path, 'r') as f: 
			for line in f: 
				if start_read:
					lexicon.add(line.strip())
				if line.strip() == "":
					start_read = True
		return lexicon

	def featurize(self, tokens):
		'''
		INPUT: list of strings
		OUTPUT: 

		Note: tokens should be a list of 
		lower-case string tokens, possibly
		including negation markings. 
		'''

		features = {}

		doc_len = len(tokens)
		assert doc_len > 0, "Can't featureize document with no tokens." 

		num_pos = sum([1 if tok in self.pos_lex else 0 for tok in tokens])
		num_neg = sum([1 if tok in self.neg_lex else 0 for tok in tokens])

		features['liu_pos'] = num_pos/doc_len
		features['liu_neg'] = num_neg/doc_len

		return features

if __name__ == "__main__":
	pass
	## USEFUL SCRAPS: 

	# get 
	#sentences = []
	#for review in reviews: 
	#	sentences.extend(get_sentences(review))




