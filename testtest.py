import selenium
from selenium import webdriver
from requests import request


linktext = []


def openLink(self, url):

    self.driver = webdriver.Chrome('chromedriver.txt')
    self.driver.maximize_window()
    self.get(url)
    self.driver.find_element_by_tag_name("body").getText()
    openLink(url='https://www.gutenberg.org/files/5200/5200-h/5200-h.htm')


#def tearDown(self):
#   self.driver.close()



print(linktext)


