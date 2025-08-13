import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv('DATABASE_URL', 
    'postgresql://pg_user:pg_password@localhost:5434/coingecko_db')

# API
COINGECKO_API_KEY = os.getenv('COINGECKO_API_KEY')
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
