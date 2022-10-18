import requests
from bs4 import BeautifulSoup
from words_scrapper.models import PageWordsCount

from words_scrapper import db


def clean_word(word_data):
	"""
	this function will clean every words that
	is having special symbols.
	"""
	symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
	for i in range(len(symbols)):
		word_data = word_data.replace(symbols[i], '')
	return word_data

def count_words(url):
	"""
	This function will get a url and
	counts the words init
	"""
	try:
		response = requests.get(url,verify=False)
		soup = BeautifulSoup(response.content)
		words_list = []

		# fetch words from p tags.....
		for each_item in soup.findAll('p'):
			for each_word_line in each_item.findAll(text=True):
				for each_word in each_word_line.split():
					word = clean_word(each_word)
					if word:
						words_list.append(word.lower())

		# fetch data from div:
		for each_item in soup.findAll('div'):
			for each_word_line in each_item.findAll(text=True):
				for each_word in each_word_line.split():
					word = clean_word(each_word)
					if word:
						words_list.append(word.lower())

		# create dict out of it
		words_count = {}
		total_words = len(words_list)
		total_unique_words = 0
		for word in words_list:
			if word in words_count:
				words_count[word] += 1
			else:
				words_count[word] = 1
				total_unique_words += 1
		# create record in database.......
		page_words_count = PageWordsCount(url=url, total_words=total_words, json_record=words_count)
		db.session.add(page_words_count)
		db.session.commit()
	except Exception as err:
		print(str(err))
		return(str(err))
