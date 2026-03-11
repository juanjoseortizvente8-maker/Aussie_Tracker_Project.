from db_connection import get_connection # <--- Tu conexión centralizada

def update_database():
    conn = None
    try:
        # Obtenemos la conexión desde el sistema de secretos
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # Añadimos la columna 'sets' para las series
        # Usamos un bloque try interno por si la columna ya existe
        print("--- ⚙️ ACTUALIZANDO ESTRUCTURA DE TABLA ---")
        sql = "ALTER TABLE gym_progress ADD (sets NUMBER DEFAULT 1)"
        
        cursor.execute(sql)
        print("✅ ÉXITO: La base de datos ahora acepta series granulares.")
        
    except Exception as e:
        # En Oracle, el error de columna duplicada es común en actualizaciones
        if "ORA-01430" in str(e):
            print("ℹ️ Nota: La columna 'sets' ya existe en 'gym_progress'.")
        else:
            print(f"❌ Error al actualizar la tabla: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    update_database()