from db_connection import get_connection # <--- Importamos tu sistema secreto
from datetime import datetime

def show_my_progress():
    conn = None
    try:
        # Usamos la conexión segura que ya sabe tus secretos
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL para traer todo ordenado por fecha
        sql = "SELECT log_date, habit_name, category, status FROM aussie_habits ORDER BY log_date DESC"
        
        print(f"\n{'DATE':<12} | {'HABIT':<25} | {'CAT':<10} | {'STATUS'}")
        print("-" * 65)
        
        for row in cursor.execute(sql):
            # Formateamos la fecha para que se vea limpia
            date_str = row[0].strftime("%Y-%m-%d")
            # Usamos emojis para el status para que sea más visual
            status_icon = "✅" if row[3].upper() == "DONE" else "❌"
            print(f"{date_str:<12} | {row[1]:<25} | {row[2]:<10} | {status_icon} {row[3]}")
            
    except Exception as e:
        print(f"❌ Error al leer los hábitos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    show_my_progress()