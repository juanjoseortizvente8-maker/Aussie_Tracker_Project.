import oracledb
import pandas as pd
from datetime import datetime
import os
from db_connection import get_connection # <--- Tu "corazón" de conexión

def backup_to_csv():
    conn = None # Inicializamos conn para evitar errores en el 'finally'
    try:
        # Crear carpeta de backups si no existe
        if not os.path.exists('backups'):
            os.makedirs('backups')
        
        # CAMBIO AQUÍ: Llamamos a tu función secreta en lugar de oracledb.connect
        conn = get_connection()
        
        if conn is None:
            return # Si no hay conexión, salimos de la función

        tables = ["gym_progress", "australia_fund", "daily_habits"]
        date_str = datetime.now().strftime("%Y-%m-%d")

        print(f"--- 📂 INICIANDO RESPALDO ({date_str}) ---")

        for table in tables:
            query = f"SELECT * FROM {table}"
            df = pd.read_sql(query, conn)
            
            file_path = f"backups/backup_{table}_{date_str}.csv"
            df.to_csv(file_path, index=False)
            print(f"✅ {table} guardado en: {file_path}")

        print("\n✨ ¡Respaldo completado! Tus datos están a salvo.")

    except Exception as e:
        print(f"❌ Error en el backup: {e}")
    finally:
        # Cerramos la conexión solo si se logró abrir
        if conn:
            conn.close()

if __name__ == "__main__":
    backup_to_csv()