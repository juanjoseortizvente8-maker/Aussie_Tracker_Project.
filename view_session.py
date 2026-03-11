import oracledb
from db_connection import get_connection # <--- Importamos tu nuevo sistema secreto

def show_session_summary(day):
    conn = None
    try:
        # Llamamos a la conexión secreta
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL: TRUNC(workout_date) quita la hora y deja solo el día
        sql = """
            SELECT exercise_name, 
                   COUNT(sets) as total_sets, 
                   AVG(weight_kg) as avg_weight, 
                   SUM(weight_kg * reps) as volume,
                   TRUNC(workout_date)
            FROM gym_progress 
            WHERE UPPER(workout_day) = UPPER(:1)
            AND TRUNC(workout_date) = TRUNC(SYSDATE)
            GROUP BY exercise_name, TRUNC(workout_date)
            ORDER BY exercise_name
        """
        
        print(f"\n{'='*75}")
        print(f"🇦🇺  RESUMEN DE HOY: {day.upper()}  🇦🇺")
        print(f"{'='*75}")
        print(f"{'EJERCICIO':<30} | {'SETS':<6} | {'PESO PROM':<10} | {'VOLUMEN'}")
        print(f"{'-'*75}")
        
        grand_total_volume = 0
        
        for row in cursor.execute(sql, [day]):
            print(f"{row[0]:<30} | {row[1]:<6} | {row[2]:<10.2f} | {row[3]:<8} kg")
            grand_total_volume += row[3]
        
        print(f"{'='*75}")
        print(f"🔥 VOLUMEN TOTAL DEL DÍA: {grand_total_volume} kg")
        print(f"{'='*75}")
            
    except Exception as e:
        print(f"❌ Error al mostrar el resumen: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    tipo = input("¿Qué sesión quieres ver? (Push/Pull/Legs): ")
    show_session_summary(tipo)