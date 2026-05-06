from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CAMPO_NOME = (By.ID, "first-name")
    CAMPO_SOBRENOME = (By.ID, "last-name")
    CAMPO_CEP = (By.ID, "postal-code")
    BOTAO_CONTINUAR = (By.ID, "continue")
    BOTAO_FINALIZAR = (By.ID, "finish")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "[data-test='error']")
    TOTAL_PEDIDO = (By.CLASS_NAME, "summary_total_label")

    def preencher_dados(self, nome, sobrenome, cep):
        self.digitar(self.CAMPO_NOME, nome)
        self.digitar(self.CAMPO_SOBRENOME, sobrenome)
        self.digitar(self.CAMPO_CEP, cep)

    def continuar(self):
        self.clicar(self.BOTAO_CONTINUAR)

    def finalizar(self):
        self.clicar(self.BOTAO_FINALIZAR)

    def obter_total(self):
        return self.texto_de(self.TOTAL_PEDIDO)

    def obter_mensagem_de_erro(self):
        return self.texto_de(self.MENSAGEM_ERRO)
