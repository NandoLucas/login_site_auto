from selenium import webdriver
from config.settings import BASE_URL, USERNAME, PASSWORD, USERNAME_FIELD_ID, PASSWORD_FIELD_ID, LOGIN_BUTTON_SELECTOR
from login import LoginBot
import logging

# Configuração do logger
logging.basicConfig(
    filename="logs/robo.log",  # Caminho do arquivo de log
    level=logging.INFO,         # Nível do log (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato do log
    datefmt="%d-%m-%Y %H:%M:%S"  # Formato de data e hora
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    # Registrar o início da execução
    logger.info("Inicializando o robô de login")

    # Configurar o driver do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        # Instanciar o robô de login
        logger.info("Criando a instância do LoginBot")
        # Executar o robô
        bot = LoginBot(driver, BASE_URL)
        # Executar o login
        logger.info("Iniciando o acesso")
        bot.login(USERNAME, PASSWORD, USERNAME_FIELD_ID, PASSWORD_FIELD_ID, LOGIN_BUTTON_SELECTOR)

    except Exception as e:
        logger.error(f"Erro durante a execução do robô: {e}")

    finally:
        # Garantir que o WebDriver seja encerrado
        logger.info("Encerrando o WebDriver")
        driver.quit()