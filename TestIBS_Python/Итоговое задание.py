from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://google.com/ncr')

    def test_search(self):
        """Открываем сайт google"""
        self.driver.get('http://google.com/ncr')
        assert 'Google' in self.driver.title

        """Ищем строку ввода и даем на ввод selenide"""
        elm = self.driver.find_element(by=By.XPATH, value='//div/input[@name="q"]')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)

        """Ищем первую ссылку и проверяем, что это selenide.org"""
        link = self.driver.find_elements(by=By.XPATH, value='//*[contains(@class, "iUh30")]')
        assert 'selenide.org' in link[0].text
        go_to_pic = self.driver.find_element(by=By.XPATH, value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        pic = self.driver.find_elements(by=By.XPATH, value='//*[contains(@class, "fxgdke")]')
        assert 'selenide.org' in pic[0].text

        """Переходим на Все и проверяем, что ссылка не изменилась"""
        go_to_all = self.driver.find_element(by=By.XPATH, value='//*[@class="NZmxZe"][1]').click()
        link2 = self.driver.find_elements(by=By.XPATH, value='//*[contains(@class, "iUh30")]')
        assert 'selenide.org' in link2[0].text

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()