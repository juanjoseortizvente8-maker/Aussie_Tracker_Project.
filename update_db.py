import oracledb

# ... (Tus credenciales jjsk1808@) ...

def add_column():
    try:
        conn = oracledb.connect(user="system", password="jjsk1808@", dsn="localhost:1521/xe")
        cursor = conn.cursor()
        # Añadimos la columna workout_day
        sql = "ALTER TABLE gym_progress ADD (workout_day VARCHAR2(20))"
        cursor.execute(sql)
        print("✅ Columna 'workout_day' añadida con éxito.")
    except Exception as e:
        print(f"⚠️ Nota: Es posible que la columna ya exista o {e}")
    finally:
        if 'conn' in locals(): conn.close()

add_column()