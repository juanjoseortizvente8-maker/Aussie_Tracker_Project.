from db_connection import get_connection # <--- Importamos tu sistema secreto
from datetime import datetime

def show_progress(exercise):
    conn = None
    try:
        # Usamos la conexión centralizada
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL para filtrar por ejercicio y ordenar de más antiguo a más reciente
        # Usamos UPPER y LIKE para que la búsqueda sea flexible
        sql = """
            SELECT workout_date, weight_kg, reps 
            FROM gym_progress 
            WHERE UPPER(exercise_name) LIKE UPPER('%' || :1 || '%')
            ORDER BY workout_date ASC
        """
        
        print(f"\n📈 PROGRESIÓN PARA: {exercise.upper()}")
        print(f"{'FECHA':<12} | {'PESO':<8} | {'REPS'}")
        print("-" * 35)
        
        rows = cursor.execute(sql, [exercise]).fetchall()
        
        if not rows:
            print(f"🔎 No se encontraron registros para '{exercise}'.")
        else:
            for row in rows:
                fecha = row[0].strftime("%d-%m-%Y")
                print(f"{fecha:<12} | {row[1]:<8} | {row[2]}")
            
    except Exception as e:
        print(f"❌ Error al leer los datos del gym: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    ex_to_check = input("¿De qué ejercicio quieres ver tu progreso?: ")
    show_progress(ex_to_check)