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
    """Get the betting odds and volumes for Betfair horse races."""

    rows = driver.find_elements_by_class_name("runner-line")

    for row in rows:
        name_elems = row.find_elements_by_class_name("runner-name")
        if len(name_elems) == 0:
            print('no names: skipping')
            continue
        name = name_elems[0].text

        runner_number = int(row.find_element_by_class_name("saddle-cloth").text)

        cells = row.find_elements_by_class_name("bet-buttons")

        for cell in cells:
            odds_text = cell.find_element_by_class_name("bet-button-price").text
            vol_text = cell.find_element_by_class_name("bet-button-size").text
            print(runner_number, name, odds_text, vol_text)



	

def ladbrokes_races_get_bet_map(driver, link):
    
    rows = driver.find_elements_by_class_name("race-table-row")

    bet_map = {}

    for row in rows:

		nums = row.find_elements_by_class_name("runner-number")
		num = nums[0].text

		name_elems = row.find_elements_by_class_name("runner-name")
		if len(name_elems) == 0:
			print('no names: skipping')
			continue
		name = name_elems[0].text
		
		odds_box_elems = row.find_elements_by_class_name("price-button-odds-price")
		odds = [float(x.text) for x in odds_box_elems]
		if len(odds) == 0:
			continue
		print((num, name, odds))
		bet_map[name] = odds

driver = webdriver.Chrome(executable_path=r'C:\Users\Thejan Elankayer\Documents\General\betting\chromedriver.exe')
driver.implicitly_wait(1)

link = "https://www.ladbrokes.com.au/racing/darwin/21b70ae9-c5f0-486d-a0e3-90870df06b2f"

driver.get(link)

page_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "runner-name"))).text


ladbrokes_races_get_bet_map(driver, link)

driver.close()

# link = "https://www.betfair.com.au/exchange/plus/horse-racing/market/1.185315447"
# driver.get(link)

# page_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "runner-name"))).text
# betfair_get_vol_map(link, driver)

# driver.close()

