import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

def clean_word(word_data):
    symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
    for i in range(len(symbols)):
        word_data = word_data.replace(symbols[i], '')
    return word_data


# We get the url
try:
    r = requests.get("https://abcdfgvhaklsdajdlsa.com")
except:
    print("kuch kaharb hua hai")
    ret
soup = BeautifulSoup(r.content)
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

print(total_words, total_unique_words)

