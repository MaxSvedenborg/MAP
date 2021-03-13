import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

Stopwordslist = stopwords.words('english')


dirty_data = "AIK should like to mention here a trouble we often encountered and which was a great worry to us both."
word_list = word_tokenize(dirty_data)



#def first_cleaning_method(word_list):

for words in word_list:
    if word_list not in Stopwordslist:
        first_cleaned_sentence = []
        first_cleaned_sentence.append(words)

        print(first_cleaned_sentence)