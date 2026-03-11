import os
import oracledb
from dotenv import load_dotenv

# Esto carga los datos de tu archivo .env
load_dotenv()

def get_connection():
    try:
        # Aquí usamos las variables secretas que pusiste en el .env
        conn = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )
        return conn
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return None