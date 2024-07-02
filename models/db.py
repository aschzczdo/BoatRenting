# db.py

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_HOST = "aws-0-eu-central-1.pooler.supabase.com"
SUPABASE_DBNAME = "postgres"
SUPABASE_PORT = 6543
SUPABASE_USER = "postgres.ykpcrlwaxxabqesnivfz"
SUPABASE_PASSWORD = "qxbGtzdsMT1F0zBa"

def postgres_connection():
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=SUPABASE_HOST,
            port=SUPABASE_PORT,
            dbname=SUPABASE_DBNAME,
            user=SUPABASE_USER,
            password=SUPABASE_PASSWORD,
        )

        # Return the connection object
        return conn

    except psycopg2.Error as e:
        # Handle connection errors
        print(f"Error connecting to PostgreSQL: {e}")
        return None
