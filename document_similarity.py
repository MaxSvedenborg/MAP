from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from urllib.request import urlopen
from math import sqrt, log
import nltk
import re
import urllib.request
import random
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Variable stopwords is created, holds the function of stopwords, and we define it to be english language.
# the stopword-function sorts away the words we don't usually want. As they are not relevant for us.
# Lemmer takes a word in the list, and returns the root-form of it, if the word is included in the wordnet list.
# Stemmer rips away the endings of the words to get it closer to a singular normal form.

stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmer = WordNetLemmatizer()

# A list of links, that is executed with random-function, to act as a vocab-book for the users book.
url_bag = ['https://www.gutenberg.org/files/84/84-0.txt',
'https://www.gutenberg.org/files/64817/64817-0.txt',
'https://www.gutenberg.org/files/11/11-0.txt',
'https://www.gutenberg.org/files/345/345-0.txt',
'https://www.gutenberg.org/files/76/76-0.txt',
'https://www.gutenberg.org/files/43/43-0.txt',
'https://www.gutenberg.org/cache/epub/5200/pg5200.txt',
]

# We give the program links to the books, that it will open up and read via requests to the server.
# As we read the book, it is now interactive for us, so we can preprocess it.
# We start with decoding it to utf-8 to exclude anomalyties and forcing the
# text to lowercase to make it easier for comparsion.
vocab_book = random.choice(url_bag)
chosen_book = 'https://www.gutenberg.org/files/64809/64809-0.txt'
request_book = urllib.request.Request(chosen_book)
request_vocab = urllib.request.Request(vocab_book)
response_book = urllib.request.urlopen(request_book)
response_vocab = urllib.request.urlopen(request_vocab)
book_text = response_book.read().decode('utf-8').lower()
vocab_text = response_vocab.read().decode('utf-8').lower()


#  placeholder here is the book we want to compare.
#  clean_tokenization-method takes the text in the books, and treats it with Nltk-extensions
#  and transforms the text into single words in a list.


def clean_tokenization(placeholder):
    return word_tokenize(placeholder)


# take the list of text, run it through clean_stem method. This preprocess-step cuts the endings of
# the words to get it into more singular form.

def clean_stem(placeholder):
    return [stemmer.stem(placeholder) for placeholder in placeholder]

# lemmer konverterar orden till sin grundform
# Lemmer-method converts the words into its root-form, if the words are found in the
# wordnet-list that is provided in the function.


def clean_lemmatization(placeholder):
    return [lemmer.lemmatize(placeholder) for placeholder in placeholder]

# stopwordsmetoden nedan sorterar bort de stopp-ord vi inte vill ha, dvs, de ord som inte tillför något.


def clean_stopwords(placeholder):
    return [word for word in placeholder if word not in stopwords]

# the stopword-function sorts away the words we don't usually want. As they are not relevant for us.


def clean_single_objects(placeholder):
    return [word for word in placeholder if len(word) > 1]

# Clean_single_objects method is where we determine what characters that should be allowed, and the ones who are not -
# are being converted into blank, null.


def clean_symbols(placeholder):
    placeholder = [re.sub('[^a-z0-9 ]', '', word) for word in placeholder]
    return placeholder

# finally, we run our books through all the preprocessing methods and return the "cleaned" list of text.


def final_clean(placeholder):
    placeholder = clean_tokenization(placeholder)
    placeholder = clean_stopwords(placeholder)
    placeholder = clean_symbols(placeholder)
    placeholder = clean_single_objects(placeholder)
    placeholder = clean_stem(placeholder)
    placeholder = clean_lemmatization(placeholder)
    return placeholder


bagOfWordsA = final_clean(book_text)
bagOfWordsB = final_clean(vocab_text)


# Create a set, which by nature contains no duplicates, of the union of bowA and bowB
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))


# First, create new dictionaries with keys from the elements of set uniqueWords and initiate the values as 0
# Secondly, iterate through each bow list and add 1 to the value of every key whenever the corresponding word appears
# in the set uniqueWords
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1


# Calculate the term frequency of each document by taking the amount of times a word appears in each document divided by
# the total number of words in the document
# First, create function calculateTF which takes two arguments numOfWord dict and bow dict
# Secondly, create a new dict tfDict and also get the length of bow dict into variable bagOfWordsCount
# Thirdly, create for loop that iterates through each word in bow dict and count each word appearance. Divide the number
# of appearances each word had in numOfWords dicts by how many words there are in bagOfWordsCount (made into a fraction)
# which is the total number of words in bow list.
def calculateTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


# Calling the function calculateTF to get the term frequency of both documents
tfA = calculateTF(numOfWordsA, bagOfWordsA)
tfB = calculateTF(numOfWordsB, bagOfWordsB)


# Calculate the inverse document frequency by dividing the log of the number of documents that contain a certain word
# Do this to get the weight of rare words across all documents in the corpus
# Firstly, create function calculateIDF with the parameter documents ([numOfWords])
# Secondly, let the var number equal the length of numOfWords and create new dictionary with keys from the elements of
# dicts numOfWords and initiate the values as 0
# Thirdly, create for loop iterating through each numOfWords. Create for loop inside the previous loop on every key
# value pair in numOfWords. Inside this loop check if value to key is greater than 0. If that's the case add 1 to the
# value in idfDict.
# Fourthly, create new for loop outside of previous iterations that loops through every key value pair in numOfWords.
# Inside the for set idf[word] to equal to the log of number divided by the keys value as a fraction. 1 is added to prevent
# division by zero which would not be possible.
def calculateIDF(documents):
    number = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = log(number / float(val) + 1)
    return idfDict


# The calculateIDF function result is stored in the variable idfNumbers
idfNumbers = calculateIDF([numOfWordsA, numOfWordsB])


# Calculate the product of tf and idf by multiplying each word's value in the corpus by the idf.
# Firstly, create function calculateTFIDF that takes two parameters, tf and idf from previous functions.
# Secondly, create for loop which iterates through every key value pair in tf. Inside this loop let the new dict equal
# each value times idfNumbers.
def calculateTFIDF(tfBagOfWords, idfNumbers):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfNumbers[word]
    return tfidf


# Call function calculateTFIDF on tfA and TFB and let dict tfidfA and tfidfB take the result.
tfidfA = calculateTFIDF(tfA, idfNumbers)
tfidfB = calculateTFIDF(tfB, idfNumbers)

# Transform tfidf dicts into lists tfidf_values and print them
tfidfA_values = list(tfidfA.values())
tfidfB_values = list(tfidfB.values())
print(tfidfA_values, tfidfB_values)


# Calculate the cosine similarity between tfidf_values lists by dividing the dot product of two vectors (tfidfA_values
# and tfidfB_values) with the multiplication of the norms of the vectors.
# Firstly, create the variables prod1, prodA1 and prodB1 that hold 0 as an int.
# Secondly, create a for loop that iterates through a zip object of tfidfA_values and tfidfB_values where each index in
# the first list is paired up with the same index of the other list.
# Thirdly, let prodA1 be the squareroot of each element in the vector tfidfA_values to create the norm of the vector.
# Let prodB1 be the squareroot of each element in the vector tfidfB_values to create the norm of the vector.
# Let prod1 be the dot product of the vectors tfidfA_values, tfidfB_values.
# Fourthly, let the variable cosine_similarity be prod1 divided by the sqrt of prodA1 times the sqrt of prodB1.
# Let all of this be in a try block and when division by zero happens it throws an exception.
try:
    prod1 = 0
    prodA1 = 0
    prodB1 = 0
    for i, j in zip(tfidfA_values, tfidfB_values):
        prodA1 += i * i
        prodB1 += j * j
        prod1 += i * j
    cosine_similarity = prod1 / ((sqrt(prodA1)) * (sqrt(prodB1)))
    print(cosine_similarity)
except:
    print(0.0)
