import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
Stopwordslist = stopwords.words('english')

book_url_list = ['https://www.gutenberg.org/files/84/84-h/84-h.htm',
'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm',
'https://www.gutenberg.org/files/11/11-h/11-h.htm',
'https://www.gutenberg.org/files/98/98-h/98-h.htm',
'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm',
'https://www.gutenberg.org/files/5200/5200-h/5200-h.htm',
'https://www.gutenberg.org/files/2542/2542-h/2542-h.htm',
'https://www.gutenberg.org/files/1080/1080-h/1080-h.htm',
]

chosen_book = 'https://www.gutenberg.org/files/64793/64793-h/64793-h.htm'

test_sentence = ["I should like to mention here a trouble we often encountered and which was a great worry to us both.",
                ]



data_set = [
    "I like to ride my bicycle",
    "I love ice-cream",
    "You are not my father"
]

dirty_data = "I should like to mention here a trouble we often encountered and which was a great worry to us both."

word_tokens = word_tokenize(dirty_data)
first_cleaned_sentence = []

for words in word_tokens:
    if words not in Stopwordslist:
        first_cleaned_sentence.append(words)


print(first_cleaned_sentence)
