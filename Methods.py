import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests
nltk.download('punkt')
nltk.download('stopwords')

Stopwordslist = stopwords.words('english')


dirty_data = "AIK should like to mention here a trouble we often encountered and which was a great worry to us both."
#word_list = word_tokenize(dirty_data)



#def first_cleaning_method(word_list):

#for words in word_list:
    #if word_list not in Stopwordslist:
        #first_cleaned_sentence = []
        #first_cleaned_sentence.append(words)

        #print(first_cleaned_sentence)

url = "https://www.gutenberg.org/files/84/84-0.txt"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
print(soup.get_text())


def convert_string(x):


    words = word_tokenize(x)
    words_cleaned = [word.lower() for word in words if (
        (not word.lower() in stopwords.words('english')) & word.isalnum())]

    return words_cleaned
a=convert_string(soup)
print (a)


soup = BeautifulSoup(open("zing.internet.accelerator.plus.txt").read())