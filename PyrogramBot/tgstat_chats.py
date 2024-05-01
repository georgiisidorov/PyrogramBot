from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from urllib3.exceptions import NewConnectionError, MaxRetryError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def hchats(keywords):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument(f"user-data-dir=C:\\Users\\Георгий\\PycharmProjects\\Courses_sale\\tgstat")

	browser = webdriver.Chrome(options=chrome_options)
	browser.delete_all_cookies()

	hrefs = []

	for keyword in keywords:
		browser.get('https://tgstat.ru/search')
		time.sleep(3)
		input_key = browser.find_element_by_id('q')
		input_key.send_keys(keyword)
		print(keyword)
		type = browser.find_element_by_id('peertype')
		type.click()
		type.find_elements_by_css_selector('option')[-1].click()
		browser.find_element_by_css_selector("button[type='submit']").click()
		time.sleep(5)
		icons = browser.find_elements_by_css_selector("li.search-channels-list-item")

		i = 0

		for icon in icons:
			try:
				ac = ActionChains(browser)
				ac.move_to_element(icon).click().perform()
				time.sleep(0.5)
				container = browser.find_elements_by_css_selector('div.posts-list')
				time.sleep(0.25)
				href = container[0].find_element_by_class_name('channel-post-title').get_attribute('href')
				hrefs.append(href.split('/channel/')[-1])
				i += 1
			except StaleElementReferenceException:
				pass
			# if i % 4 == 0:
			# 	browser.find_element_by_css_selector('a.arrow-holder.right').click()

	browser.close()
	browser.quit()

	# return list(set(hrefs))

	print(list(set(hrefs)))



hchats(['сливы курсов', 'удаленка', 'фриланс', 'образование', 'работа'])
