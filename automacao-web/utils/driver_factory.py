from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def criar_driver(headless=False):
    options = Options()

    if headless:
        # flags necessarias pra rodar no ubuntu do github actions
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        # desativa popups do gerenciador de senhas na execucao local
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver
