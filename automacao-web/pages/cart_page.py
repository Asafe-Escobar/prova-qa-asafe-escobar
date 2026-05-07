from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pages.base_page import BasePage


class CartPage(BasePage):

    URL_CHECKOUT = "https://www.saucedemo.com/checkout-step-one.html"

    ITENS_NO_CARRINHO = (By.CLASS_NAME, "cart_item")
    NOMES_DOS_ITENS = (By.CLASS_NAME, "inventory_item_name")
    BOTAO_CHECKOUT = (By.ID, "checkout")

    def quantidade_de_itens(self):
        return len(self.driver.find_elements(*self.ITENS_NO_CARRINHO))

    def listar_nomes_dos_itens(self):
        elementos = self.driver.find_elements(*self.NOMES_DOS_ITENS)
        return [el.text for el in elementos]

    def finalizar_compra(self):
        try:
            self.clicar(self.BOTAO_CHECKOUT)
        except WebDriverException:
            self.driver.get(self.URL_CHECKOUT)
        self.aguardar_url_conter("checkout")
