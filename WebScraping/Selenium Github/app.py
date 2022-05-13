from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver_win32' / 'chromedriver.exe'

print(CHROME_DRIVER_PATH)


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=Perfil')
        self.chrome_service = Service(
            executable_path=CHROME_DRIVER_PATH,
        )
        self.chrome = webdriver.Chrome(
            service=self.chrome_service,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element(By.CSS_SELECTOR,
                                              'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex')
            # self.chrome.find_element_by_css_selector(
            # 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element(By.CSS_SELECTOR,
                                              'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form')
            # self.chrome.find_element_by_css_selector( 'body > div.position-relative.js-header-wrapper > header
            # > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')
            # btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('mateusvc11@gmail.com')
            input_password.send_keys('1424738wsE')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perfil()
    chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    # chrome.verifica_usuario('mateusvdcastro')

    sleep(5)
    chrome.sair()
