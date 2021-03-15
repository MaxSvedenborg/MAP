import nltk
from nltk.corpus import stopwords
from math import sqrt, log

# Gather stopwords with no significance to the essence of the book
nltk.download('stopwords')
stopwords.words('english')

# Corpus
documentA = 'the sky is red'
documentB = 'the sky is'

# Split the strings by each spacing into lists
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

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
# First, create function which takes two arguments numOfWord dict and bow dict
# Secondly, create a new dict tfDict and also get the length of bow dict into variable bagOfWordsCount
# Thirdly, create for loop that iterates through each word in bow dict and count each word appearance. Divide the number
# of appearances each word had in numOfWords dicts by how many words there are in bagOfWordsCount (made into a fraction)
# which is the total number of words in bow list.
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


# Calling the function computeTF to get the term frequency of both documents
tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)


# Calculate the inverse document frequency by dividing the log of the number of documents that contain a certain word
# Do this to get the weight of rare words across all documents in the corpus
# Firstly, create function computeIDF with the parameter documents ([numOfWords])
# Secondly, let the var N equal the length of numOfWords and create new dictionary with keys from the elements of dicts
# numOfWords and initiate the values as 0
# Thirdly, create for loop iterating through each numOfWords. Create for loop inside the previous loop on every key
# value pair in numOfWords. Inside this loop check if value to key is greater than 0. If that's the case add 1 to the
# value in idfDict.
# Fourthly, create new for loop outside of previous iterations that loops through every key value pair in numOfWords.
# Inside the for set idf[word] to equal to the log of N divided by the keys value as a fraction. 1 is added to prevent
# division by zero which would not be possible.
def computeIDF(documents):
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = log(N / float(val) + 1)
    return idfDict


# The computeIDF function result is stored in the variable idfs
idfs = computeIDF([numOfWordsA, numOfWordsB])


# Calculate the product of tf and idf by multiplying each word's value in the corpus by the idf.
# Firstly, create function computeTFIDF that takes two parameters, tf and idf from previous functions.
# Secondly, create for loop which iterates through every key value pair in tf. Inside this loop let the new dict equal
# each value times idfs.
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


# Call function computeTFIDF on tfA and TFB and let dict tfidfA and tfidfB take the result.
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)


# Transform tfidf dicts into lists tfidf_values and print them
tfidfA_values = list(tfidfA.values())
tfidfB_values = list(tfidfB.values())
print(tfidfA_values, tfidfB_values)

# Calculate the cosine similarity between tfidf_values lists by dividing the dot product of two vectors (tfidfA_values
# and tfidfB_values) with the multiplication of the norms of the vectors.
# Firstly, create the variables sum1, suma1 and sumb1 that hold 0 as an int.
# Secondly, create a for loop that iterates through a zip object of tfidfA_values and tfidfB_values where each index in
# the first list is paired up with the same index of the other list.
# Thirdly, let suma1 be the squareroot of each element in the vector tfidfA_values to create the norm of the vector.
# Let sumb1 be the squareroot of each element in the vector tfidfB_values to create the norm of the vector.
# Let sum1 be the dot product of the vectors tfidfA_values, tfidfB_values.
# Fourthly, let the variable cosine_similarity be sum1 divided by the squareroot of suma1 times the squareroot of sumb1.
# Let all of this be in a try block and when division by zero happens it throws an exception.
try:
    sum1 = 0
    suma1 = 0
    sumb1 = 0
    for i, j in zip(tfidfA_values, tfidfB_values):
        suma1 += i * i
        sumb1 += j * j
        sum1 += i * j
    cosine_similarity = sum1 / ((sqrt(suma1)) * (sqrt(sumb1)))
    print(cosine_similarity)
except:
    print(0.0)



