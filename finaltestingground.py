import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from urllib.request import urlopen
import urllib.request
nltk.download('punkt')
nltk.download('stopwords')

# Gather stopwords with no significance to the essence of the book
stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()  #  tar emot nltk-format eller sträng. vi "döper om" den till stemmer
lemma = WordNetLemmatizer()  # tar ett ord och ger tillbaks root-ordet av det om det finns i listan wordnet. ett bra sätt att standardisera alla ord och ta bort unika stavelser.

vocab_book = 'https://www.gutenberg.org/files/64317/64317-0.txt'  # inmatad bok.txt fil utf-8, benämns nu vocab_book
chosen_book = 'https://www.gutenberg.org/files/64809/64809-0.txt'  # inmatad bok.txt fil utf-8, benämns nu chosen_book
request_book = urllib.request.Request(chosen_book)
request_vocab = urllib.request.Request(vocab_book)# skickar request till gutenbergs server om att vi vill få den inmatade boken chosen_book
response_book = urllib.request.urlopen(request_book)                  # vi skickar en request om att öppna boken vi precis hämtat, chosen_book
response_vocab = urllib.request.urlopen(request_vocab)
book_text = response_book.read().decode('utf-8').lower()  # book_text variabeln skapas, innehåller nu en read samt en decode av chosen_book till utf-8. tack vare read kan vi arbeta med boken?.
vocab_text = response_vocab.read().decode('utf-8').lower()





def clean_tokenization(placeholder):   #  här har vi placeholder, för det är ju faktiskt värdet inom parantes av metoden vi kör som spelar roll
    return word_tokenize(placeholder)    #  placeholder här med, i och med att det är metodens värde som vi anger på annan plats som ges tillbaks här
#  ovan metod tar texten och behandlar det enligt nltk, och förvandlar text till split text, enskilda ord.


def clean_stem(placeholder):
    return [stemmer.stem(placeholder) for placeholder in placeholder]  # ta boken, kör den genom porterstemmern dvs vi kapar ?ändelser?,


def clean_lemmatization(placeholder):
    return [lemma.lemmatize(placeholder) for placeholder in placeholder]  # converts the word into root form


def clean_stopwords(placeholder):
    return [word for word in placeholder if word not in stopwords]


def clean_single_objects(placeholder):
    return [word for word in placeholder if len(word) > 1]


def remove_symbols(placeholder):
    placeholder = [re.sub('[^a-z0-9 ]', '', word) for word in placeholder]
    return placeholder


def max_clean(placeholder):
    placeholder = clean_tokenization(placeholder)
    placeholder = clean_stopwords(placeholder)
    placeholder = remove_symbols(placeholder)
    placeholder = clean_single_objects(placeholder)
    placeholder = clean_stem(placeholder)
    placeholder = clean_lemmatization(placeholder)
    return placeholder


print(max_clean(book_text))
print(max_clean(vocab_text))

#print(max_clean(book_text))
#print(ig.number_to_words(word))