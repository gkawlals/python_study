from selenium import webdriver
import requests
import csv

# from bs4 import BeautifulSoup

csv_file = "starbucks_crawling.csv"
csv_open = open(csv_file, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('drink'))

driver = webdriver.Chrome()

url = "https://www.starbucks.co.kr/menu/drink_list.do"
driver.get(url)

xpath = "//div[@class='product_result_wrap product_result_wrap01']//div[@class='product_list']//ul/li[@class='menuDataSet']//dd[contains(text())]"
drinks_info = driver.find_elements_by_xpath(xpath)


for drink  in drinks_info:
    title = drink.get_attribute('alt')


    csv_writer.writerow((title))