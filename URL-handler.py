import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from selenium import webdriver
from nltk import word_tokenize
import selenium
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from num2words import num2words

nltk.download('punkt')
nltk.download('stopwords')
Stopwordslist = stopwords.words('english')

book_url_list = ['https://www.gutenberg.org/files/84/84-0.txt',
'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm',
'https://www.gutenberg.org/files/11/11-h/11-h.htm',
'https://www.gutenberg.org/files/98/98-h/98-h.htm',
'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm',
'https://www.gutenberg.org/files/5200/5200-h/5200-h.htm',
'https://www.gutenberg.org/files/2542/2542-h/2542-h.htm',
'https://www.gutenberg.org/files/1080/1080-h/1080-h.htm',
]



test_sentence = ["I should like to mention here a trouble we often encountered and which was a great worry to us both.",
                ]
chosen_book = 'https://www.gutenberg.org/files/64812/64812-0.txt'


data_set = [
    "I like to ride my bicycle",
    "I love ice-cream",
    "You are not my father"
]

dirty_data = "I should like to mention here a trouble we often encountered and which was a great worry to us both."

word_tokens = word_tokenize(dirty_data)
#first_cleaned_sentence = []

#for words in word_tokens:
    #if words not in Stopwordslist:
        #first_cleaned_sentence.append(words)

second_book = ('https://www.gutenberg.org/files/64809/64809-0.txt')
#print(first_cleaned_sentence)
#rint(Stopwordslist)


#def tokenization(chosen_book):

   # driver = webdriver.Chrome('chromedriver.txt')
   # driver.get(chosen_book)
   # read_text = driver.find_element_by_tag_name('body')
   # book_text = read_text.text
   # return book_text.split()


#def stemming(chosen_book):

    #stemmer = PorterStemmer()
   # stemmed = stemmer.stem(chosen_book)

    #return stemmed
#print(stemming(chosen_book))

#def lemetization(chosen_book):
   # lemmatizer = WordNetLemmatizer()
   # lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
   # return lemmatized


#def done_text(chosen_book):
   # chosen_book = tokenization(chosen_book)
   # chosen_book = stemming(chosen_book)
   # chosen_book = lemetization(chosen_book)

   #return chosen_book


def tokenization(chosen_book):
    driver = webdriver.Chrome('chromedriver.txt')
    driver.get(chosen_book)
    read_text = driver.find_element_by_tag_name('body')
    book_text = read_text.text

    cleaned = re.sub('\W+', ' ', book_text).lower()
    tokenized = word_tokenize(cleaned)
    return tokenized


def stemmer(chosen_book):
    driver = webdriver.Chrome('chromedriver.txt')
    driver.get(chosen_book)
    read_text = driver.find_element_by_tag_name('body')
    book_text = read_text.text

    cleaned = re.sub('\W+', ' ', book_text).lower()
    tokenized = word_tokenize(cleaned)

    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(book_text) for book_text in tokenized]
    return stemmed

def lemmer(chosen_book):
    driver = webdriver.Chrome('chromedriver.txt')
    driver.get(chosen_book)
    read_text = driver.find_element_by_tag_name('body')
    book_text = read_text.text

    cleaned = re.sub('\W+', ' ', book_text).lower()
    tokenized = word_tokenize(cleaned)

    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(book_text) for book_text in tokenized]
    return lemmatized

def cleaned_text(chosen_book):
    driver = webdriver.Chrome('chromedriver.txt')
    driver.get(chosen_book)
    read_text = driver.find_element_by_tag_name('body')
    book_text = read_text.text
    chosen_book = tokenization(book_text)
    chosen_book = lemmer(book_text)
    chosen_book = stemmer(book_text)
    return chosen_book

print(cleaned_text(chosen_book))









#def get_book_text_from_url(input_book):
 #   book_text_list = []
  #  list = read_text(input_book)
   # list.append(book_text_list)
    #return book_text_list


   # book_text = read_text.text.append()
#get_book_text_from_url(book_url_list)



#driver = webdriver.Chrome('chromedriver.txt')
#chosen_book = "https://www.gutenberg.org/files/84/84-0.txt"
#openbooklink = driver.get(chosen_book)
#read_text = driver.find_element_by_tag_name('body')
#book_text = read_text.text

   # cleaned = re.sub('\W+', ' ', book_text)
  #  tokenized_book = word_tokenize(cleaned)
  #  return tokenized_book

#b = get_book_text_from_url(second_book)
#print(b)
#a = read_text(chosen_book)
#print(a)

#cleaned = re.sub('\W+', ' ', chosen_book)
#tokenized = word_tokenize(cleaned)
#def tokenization(chosen_book):
 #   cleaned = re.sub('\W+', ' ', chosen_book)
  #  tokenized = word_tokenize(cleaned)
   # return tokenized



#def lemetization():
 #   lemmatizer = WordNetLemmatizer()
  #  lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
   # return lemmatized

