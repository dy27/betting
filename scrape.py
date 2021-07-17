from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BetTypeConversionTable:
	pass

class Event:
	def __init__(self, link):
		self.link = link
		self.bet_odds_map = None
		self.datetime = None


class EventMonitor:
	def __init__(self, events):
		self.events = events
		self.bet_pairs = None

		# Outcome Table
		# Outcome | Bet1 | Bet2 | ...
		# 
		self.outcome_table = None

		

def betfair_get_vol_map(link, driver=None):
	rows = driver.find_elements_by_class_name("runner-line")

	for row in rows:
		name_elems = row.find_elements_by_class_name("runner-name")
		if len(name_elems) == 0:
			print('no names: skipping')
			continue
		name = name_elems[0].text
		odds_box_elems = row.find_elements_by_class_name("runner-fixed-odds")
		if len(odds_box_elems) == 0:
			print('no odds: skipping')
			continue
		odds_box = odds_box_elems[0]
		odds = odds_box.find_elements_by_class_name("price-button-odds-price")
		odds = [float(x.text) for x in odds]
		print(name, odds)


def ladbrokes_races_get_bet_map(driver, link):
	
	rows = driver.find_elements_by_class_name("race-table-row")

	bet_map = {}

	for row in rows:
		name_elems = row.find_elements_by_class_name("runner-name")
		if len(name_elems) == 0:
			print('no names: skipping')
			continue
		name = name_elems[0].text
		odds_box_elems = row.find_elements_by_class_name("price-button-odds-price")
		odds = [float(x.text) for x in odds_box_elems]
		if len(odds) == 0:
			continue
		print((name, odds))
		bet_map[name] = odds






driver = webdriver.Chrome(executable_path=r'C:\Users\Thejan Elankayer\Documents\General\betting\chromedriver.exe')
driver.implicitly_wait(1)

link = "https://www.ladbrokes.com.au/racing/lismore/973c767f-1645-4b04-99d4-3839531a79a1"

driver.get(link)

page_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "runner-name"))).text


ladbrokes_races_get_bet_map(driver, link)

driver.close()


