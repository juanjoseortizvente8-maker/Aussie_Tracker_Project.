from db_connection import get_connection # <--- Tu conexión segura

def fix_my_gains():
    conn = None
    try:
        # Obtenemos la conexión desde el corazón del proyecto
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # Le decimos a Oracle: "Donde el día esté vacío, ponle 'Push'"
        sql = "UPDATE gym_progress SET workout_day = 'Push' WHERE workout_day IS NULL"
        
        cursor.execute(sql)
        
        # Guardamos los cambios
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ ¡Reparado! Se actualizaron {cursor.rowcount} ejercicios al día 'Push'.")
        else:
            print("ℹ️ No se encontraron registros con el día vacío. Todo está en orden.")
        
    except Exception as e:
        print(f"❌ Error al intentar reparar los datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_my_gains()