# Feature tests for Calculator UI using Selenium
# Run with: python -m unittest test_calculator_ui.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalculatorUITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Update path to your local ChromeDriver if needed
        cls.driver = webdriver.Chrome()
        cls.driver.get('file:///C:/Users/rcrd_/Desktop/test_calc/calculator/calculator.html')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # Reset calculator before each test
        ac_btn = self.driver.find_element(By.XPATH, "//button[text()='AC']")
        ac_btn.click()
        time.sleep(0.2)

    def get_display(self):
        return self.driver.find_element(By.CLASS_NAME, 'display').text

    def click_buttons(self, sequence):
        for label in sequence:
            btn = self.driver.find_element(By.XPATH, f"//button[text()='{label}']")
            btn.click()
            time.sleep(0.1)

    def test_addition(self):
        self.click_buttons(['2', '+', '3', '='])
        self.assertEqual(self.get_display(), '5')

    def test_subtraction(self):
        self.click_buttons(['7', '-', '4', '='])
        self.assertEqual(self.get_display(), '3')

    def test_multiplication(self):
        self.click_buttons(['6', '*', '5', '='])
        self.assertEqual(self.get_display(), '30')

    def test_division(self):
        self.click_buttons(['8', '/', '2', '='])
        self.assertEqual(self.get_display(), '4')

    def test_division_by_zero(self):
        self.click_buttons(['9', '/', '0', '='])
        self.assertEqual(self.get_display(), 'Error')

    def test_decimal_input(self):
        self.click_buttons(['1', '.', '5', '+', '2', '.', '5', '='])
        self.assertEqual(self.get_display(), '4')

    def test_percent(self):
        self.click_buttons(['5', '0', '%'])
        self.assertEqual(self.get_display(), '0.5')

    def test_delete(self):
        self.click_buttons(['1', '2', 'DEL'])
        self.assertEqual(self.get_display(), '1')

    def test_clear(self):
        self.click_buttons(['7', '+', '3', 'AC'])
        self.assertEqual(self.get_display(), '0')

if __name__ == '__main__':
    unittest.main()
