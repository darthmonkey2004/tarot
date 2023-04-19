from selenium import webdriver
from selenium.webdriver import ChromeOptions
from urllib.parse import unquote
from bs4 import BeautifulSoup as bs
from random import randint
import time

class reading():
	def __init__(self, headless=True):
		self.cards = []
		self.opts = ChromeOptions()
		if headless:
			self.opts.add_argument('--headless')
		self.driver = webdriver.Chrome(options=self.opts)
		self.html = None

	def get_reading_data(self, url="https://www.tarot.com/readings-reports/tarot-readings/free/love"):
		0self.html = self.get_reading_data()
		self.driver.get(url)
		self.html = bs(self.driver.page_source, 'html.parser')
		return self.html

	def shuffle(self, html=None, duration=5):
		if html is not None:
			self.html = html
		self.html.find_element(by='xpath', value="//button[@class=\"shuffle-button\"]").click()
		time.sleep(duration)
		self.html.find_element(by='xpath', value="//button[@class=\"shuffle-button\"]").click()
		return

	def rdm(self):
		return randint(1,78)

	def pick_card(idx=None):
		if idx is None:
			idx = self.rdm()
			self.cards.append(idx)
			self.html.find_element(by='xpath', value=f"//tarot-reading-deck-card[@card_id=\"{idx}\"]").click()

if __name__ == "__main__":
	reading = reading(headless=False)
	print(reading)
