import data as data
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from urllib.request import urlopen
import urllib.request

chosen_book = 'https://www.gutenberg.org/files/64809/64809-0.txt'
request = urllib.request.Request(chosen_book)
response = urllib.request.urlopen(request)
book_text = response.read().decode('utf-8')
book_text_ordered_list = book_text.split()

stemmer = PorterStemmer()
lemma = WordNetLemmatizer()


def clean_tokenization(token):
    return word_tokenize(token)


def clean_stem(token):
    return [stemmer.stem(chosen_book) for chosen_book in token]


def clean_lemmatization(token):
    return [lemma.lemmatize(chosen_book) for chosen_book in token]


def clean_review(book_text_ordered_list):
    book_text_ordered_list = clean_tokenization(book_text_ordered_list)
    book_text_ordered_list = clean_stem(book_text_ordered_list)
    book_text_ordered_list = clean_lemmatization(book_text_ordered_list)
    return book_text_ordered_list

#print(clean_review(chosen_book))
print(clean_review(book_text_ordered_list))




