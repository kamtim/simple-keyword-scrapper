from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

import re

driverPath = '/Users/study_kam/Downloads/chromedriver'

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def open_google():
  opts = Options()
  opts.headless = True

  driver = webdriver.Chrome(driverPath, options=opts)
  driver.get("http://www.google.com/")

  return driver


def google_scrapper_autocomplete(name):
  answers = []

  driver = open_google()

  search = driver.find_element_by_name("q")
  search.send_keys(name)

  # for the autocomplete block to appear
  time.sleep(1)

  autocomplete_results = driver.find_elements_by_class_name("sbct")
  # The last element is text "Delete"
  autocomplete_results.pop()

  for i in autocomplete_results:
    answers.append(cleanhtml(i.get_attribute("innerText")))

  return answers

def google_scrapper_results(name):
  answers = []

  driver = open_google()

  search = driver.find_element_by_name("q")
  search.send_keys(name)

  search.send_keys(Keys.RETURN)
  results = driver.find_elements_by_tag_name("h3")
  for i in results:
    answers.append(cleanhtml(i.get_attribute("innerHTML")))


  return answers