from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self, url):
        self.driver.get(url)

    def encontrar(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def rolar_ate(self, elemento):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)

    def clicar(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        self.rolar_ate(elemento)
        try:
            elemento.click()
        except ElementClickInterceptedException:
            # fallback pra quando algum elemento cobre o botao
            self.driver.execute_script("arguments[0].click();", elemento)

    def digitar(self, locator, texto):
        elemento = self.encontrar(locator)
        self.rolar_ate(elemento)
        elemento.clear()
        elemento.send_keys(texto)

    def texto_de(self, locator):
        return self.encontrar(locator).text

    def esta_visivel(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
