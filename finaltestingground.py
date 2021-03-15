import data as data
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from urllib.request import urlopen
import urllib.request
nltk.download('punkt')

chosen_book = 'https://www.gutenberg.org/files/64809/64809-0.txt'  # inmatad bok.txt fil utf-8, benämns nu chosen_book
request = urllib.request.Request(chosen_book)               # skickar request till gutenbergs server om att vi vill få den inmatade boken chosen_book
response = urllib.request.urlopen(request)                  # vi skickar en request om att öppna boken vi precis hämtat, chosen_book
book_text = response.read().decode('utf-8').lower()  # book_text variabeln skapas, innehåller nu en read samt en decode av chosen_book till utf-8. tack vare read kan vi arbeta med boken?.


stemmer = PorterStemmer()  #  tar emot nltk-format eller sträng. vi "döper om" den till stemmer
lemma = WordNetLemmatizer()  # tar ett ord och ger tillbaks root-ordet av det om det finns i listan wordnet. ett bra sätt att standardisera alla ord och ta bort unika stavelser.


def clean_tokenization(placeholder):   #  här har vi placeholder, för det är ju faktiskt värdet inom parantes av metoden vi kör som spelar roll
    return word_tokenize(placeholder)    #  placeholder här med, i och med att det är metodens värde som vi anger på annan plats som ges tillbaks här
#  ovan metod tar texten och behandlar det enligt nltk, och förvandlar text till split text, enskilda ord.


def clean_stem(placeholder):
    return [stemmer.stem(placeholder) for placeholder in placeholder]  #ta boken, kör den genom porterstemmern dvs vi kapar ?ändelser?,


def clean_lemmatization(placeholder):
    return [lemma.lemmatize(placeholder) for placeholder in placeholder]


def max_clean(placeholder):
    placeholder = clean_tokenization(placeholder)
    placeholder = clean_lemmatization(placeholder)
    placeholder = clean_stem(placeholder)

    return placeholder


print(max_clean(book_text))
