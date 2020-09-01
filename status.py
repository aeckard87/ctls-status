"""
A simple selenium test example written by python
"""

import os
import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
from requests.exceptions import MissingSchema


class TestStatus(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()


    def test_status(self):
        url = "https://status.educationincites.com"
        self.driver.get(url)
        # response = requests.get(url, verify=False) #in case ctls fails to update cert use this
        response = requests.get(url)
        self.assertEqual(response.status_code,200, url + " is not available!")

        try:
            elements = self.driver.find_elements_by_xpath('//table[@class=\'table\']//tr')
            total = len(elements)
            for i in range(2,total):
                element_title = self.driver.find_element_by_xpath('//table[@class=\'table\']//tr[' + str(i) + ']/td[1]').text
                element_state = self.driver.find_element_by_xpath('//table[@class=\'table\']//tr[' + str(i) + ']/td[2]').text
                print( element_title + ": " + element_state)
                self.assertEqual(element_state, "Online", element_title + " is offline!")
        except NoSuchElementException as ex:
            self.fail('Unable to determine status')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStatus)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
