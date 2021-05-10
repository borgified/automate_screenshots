#!/usr/bin/env python

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('https://microsoft.com')
browser.save_screenshot('screenshot.png')
browser.quit()
