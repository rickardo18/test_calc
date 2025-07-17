import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalculatorFeatureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('file:///c:/Users/rcrd_/Desktop/test_calc/calculator/calculator.html')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def click_button(self, label):
        buttons = self.driver.find_elements(By.CLASS_NAME, 'btn')
        for btn in buttons:
            if btn.text == label:
                btn.click()
                time.sleep(0.2)
                return
        raise Exception(f'Button {label} not found')

    def get_result(self):
        return self.driver.find_element(By.CLASS_NAME, 'result').text

    def test_addition(self):
        self.click_button('Ac')
        self.click_button('2')
        self.click_button('+')
        self.click_button('3')
        self.click_button('=')
        result = self.get_result()
        self.assertIn('=5', result)

    def test_subtraction(self):
        self.click_button('Ac')
        self.click_button('7')
        self.click_button('-')
        self.click_button('4')
        self.click_button('=')
        result = self.get_result()
        self.assertIn('=3', result)

    def test_multiplication(self):
        self.click_button('Ac')
        self.click_button('6')
        self.click_button('*')
        self.click_button('8')
        self.click_button('=')
        result = self.get_result()
        self.assertIn('=48', result)

    def test_division(self):
        self.click_button('Ac')
        self.click_button('9')
        self.click_button('/')
        self.click_button('3')
        self.click_button('=')
        result = self.get_result()
        self.assertIn('=3', result)

    def test_decimal(self):
        self.click_button('Ac')
        self.click_button('7')
        self.click_button('.')
        self.click_button('5')
        self.click_button('+')
        self.click_button('2')
        self.click_button('.')
        self.click_button('5')
        self.click_button('=')
        result = self.get_result()
        self.assertIn('=10', result)

    def test_clear(self):
        self.click_button('Ac')
        self.click_button('8')
        self.click_button('Ac')
        result = self.get_result()
        self.assertEqual(result, '')

    def test_backspace(self):
        self.click_button('Ac')
        self.click_button('9')
        self.click_button('←')
        result = self.driver.find_element(By.CLASS_NAME, 'expression').text
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
