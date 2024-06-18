import os
from dotenv import load_dotenv
load_dotenv()

DATABASE = 'sqlite:///' + os.getenv('DATABASE')