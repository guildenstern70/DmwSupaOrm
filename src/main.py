"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python

    @author: Alessio Saltarin

"""
import os

import sqlalchemy
from sqlalchemy.pool import NullPool
from sqlalchemy import text
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()
DB_URL = os.getenv('DB_URL')

if __name__ == '__main__':
    print("DmwSupaOrm v.0.0.1")
    version = sqlalchemy.__version__
    print("-- SQLAlchemy version:", version)

    engine = sqlalchemy.create_engine(DB_URL, client_encoding='utf8', poolclass=NullPool)
    print("-- Connecting to database...")
    with engine.connect() as conn:
        result = conn.execute(text("select 1"))  # execute a simple query
        print(result.all())
    print("-- Connection closed.")