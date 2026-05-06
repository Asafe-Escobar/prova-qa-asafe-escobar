from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):

    TITULO_SUCESSO = (By.CLASS_NAME, "complete-header")

    def obter_titulo_sucesso(self):
        return self.texto_de(self.TITULO_SUCESSO)

    def compra_foi_finalizada(self):
        return self.esta_visivel(self.TITULO_SUCESSO)
