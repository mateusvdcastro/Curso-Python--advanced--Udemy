import selenium
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup


class Instagram:
    def __init__(self):
        self.anchors1 = []
        self.driver_path = 'chromedriver.exe'
        self.driver = webdriver.Chrome(
            self.driver_path
        )

    def acessa(self, site):
        self.driver.get(site)

    def faz_login(self):
        try:
            username = self.driver.find_element_by_name('username')
            password= self.driver.find_element_by_name('password')
            time.sleep(2)
            username.clear()
            username.send_keys('python_overview')
            password.clear()
            password.send_keys('1424738wsE')
            btn_login = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)

    def fecha_alerta(self):
        time.sleep(5)
        alert = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        alert.click()
        alert2 = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        alert2.click()

    def buscar(self):
        searchbox = self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        searchbox.clear()
        keyword = "engenharia_deprod"
        searchbox.send_keys(keyword)
        time.sleep(5)
        my_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword + "/')]")))
        my_link.click()

    def scroll(self, num):
        n_scrolls = num
        for j in range(0, n_scrolls):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            anchors = self.driver.find_elements_by_tag_name('a')
            anchors = [a.get_attribute('href') for a in anchors]
            anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
            self.anchors1 = anchors[:]

            print('Encontrei ' + str(len(anchors)) + ' links de imagens')

    def curtidas(self):
        users = []
        lista = []
        for a in self.anchors1:
            self.driver.get(a)
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/a').click()
            except Exception:
                pass

            time.sleep(2)

            elems = self.driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")

            for elem in elems:
                users.append(elem.get_attribute('title'))
                self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
                time.sleep(0.5)

            lista.append(users[:])
            users.clear()

        print(lista)
        print(len(lista))


if __name__ == '__main__':
    driver = Instagram()
    driver.acessa('http://www.instagram.com')
    time.sleep(2)
    driver.faz_login()
    driver.fecha_alerta()
    driver.buscar()
    driver.scroll(1)
    driver.curtidas()
