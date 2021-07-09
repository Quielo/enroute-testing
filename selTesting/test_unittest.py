import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Sample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("http://demo.guru99.com/test/newtours/")

    def test_sample(self):
        print("Test")
        assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()