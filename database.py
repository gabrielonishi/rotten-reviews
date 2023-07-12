from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv(override=True)

username = os.getenv('MD_DB_USERNAME')
password = os.getenv('MD_DB_PASSWORD')
database = os.getenv('MD_DB_DATABASE')
server = os.getenv('MD_DB_SERVER')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8mb4"

# Faz a conexão com a base de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Apenas menciona a classe, ainda não cria uma instância dela (sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Outra classe. Depois vai ser utilizada para criar os modelos
Base = declarative_base()