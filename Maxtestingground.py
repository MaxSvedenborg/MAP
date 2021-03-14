import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = stopwords.words('english')
URL_LIST = ['https://www.gutenberg.org/files/25830/25830-h/25830-h.htm',
            'https://www.gutenberg.org/files/84/84-h/84-h.htm',
            'https://www.gutenberg.org/files/32069/32069-h/32069-h.htm',
            'https://www.gutenberg.org/files/19362/19362-h/19362-h.htm',
            'https://www.gutenberg.org/files/64783/64783-h/64783-h.htm',
            'https://www.gutenberg.org/files/64791/64791-h/64791-h.htm',
            'https://www.gutenberg.org/files/64790/64790-h/64790-h.htm',
            'https://www.gutenberg.org/files/2610/2610-h/2610-h.htm',
            'https://www.gutenberg.org/files/32300/32300-h/32300-h.htm',
            'https://www.gutenberg.org/files/83/83-h/83-h.htm'
            ]

chosen_book = 'https://www.gutenberg.org/files/103/103-h/103-h.htm'


def pickle_all_urls():
    for url in URL_LIST:
        full_path = get_page(url)
        soup = load_page(full_path)

openbooklink = driver.get(url)