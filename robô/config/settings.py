import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do site e elementos
BASE_URL = os.getenv("BASE_URL", "https://example.com/login")
USERNAME_FIELD_ID = os.getenv("USERNAME_FIELD_ID", "username_input_id")
PASSWORD_FIELD_ID = os.getenv("PASSWORD_FIELD_ID", "password_input_id")
LOGIN_BUTTON_SELECTOR = os.getenv("LOGIN_BUTTON_SELECTOR", "login_button_selector")

# Credenciais
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
