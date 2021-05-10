#!/usr/bin/env python

from selenium import webdriver
#browser = webdriver.Firefox()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


browser = webdriver.Chrome(options=chrome_options)
type(browser)
browser.get('https://microsoft.com')
browser.save_screenshot('screenshot.png')
browser.quit()
