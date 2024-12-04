from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Configuração do logger
logger = logging.getLogger(__name__)

class LoginBot:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def login(self, username, password, username_field_id, password_field_id, login_button_selector):
        try:
            logger.info(f"Acessando a URL: {self.base_url}")
            self.driver.get(self.base_url)

            # Esperar pelo campo de username
            logger.info("Aguardando o campo de nome de usuário ficar disponível")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, username_field_id))
            )

            # Preencher o formulário
            logger.info("Preenchendo o campo de nome de usuário")
            self.driver.find_element(By.ID, username_field_id).send_keys(username)
            logger.info("Preenchendo o campo de senha")
            self.driver.find_element(By.ID, password_field_id).send_keys(password)

            # Submeter o formulário
            logger.info("Clicando no botão de login")
            self.driver.find_element(By.CSS_SELECTOR, login_button_selector).click()

            # Verificar se houve redirecionamento (alterar de acordo com o site)
            logger.info("Verificando se o login foi bem-sucedido")
            WebDriverWait(self.driver, 10).until(EC.url_changes(self.base_url))
            logger.info("Login realizado com sucesso!")

        except TimeoutException:
            logger.error("Tempo limite excedido ao tentar realizar o login")
        except Exception as e:
            logger.error(f"Erro inesperado durante o login: {e}")
        finally:
            logger.info("Encerrando a execução do LoginBot")
