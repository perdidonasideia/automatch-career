# src/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env localmente

# Configurações do LinkedIn (opcional para testes locais)
LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

# Configurações do Notion
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# Configurações do Scraper
REQUEST_DELAY = 2  # segundos entre requests
MAX_JOBS_PER_SOURCE = 10
