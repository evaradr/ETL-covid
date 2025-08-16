from dotenv import load_dotenv
import os



# Load environment variables from .env fileload_dotenv()
load_dotenv()
# Access environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')