from db_connection import get_connection # <--- Tu conexión segura y secreta

def record_lift(day, exercise, weight, reps):
    conn = None
    try:
        # Obtenemos la conexión centralizada
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL: workout_day, exercise_name, weight_kg, reps
        sql = """INSERT INTO gym_progress (workout_day, exercise_name, weight_kg, reps) 
                VALUES (:1, :2, :3, :4)"""
        
        cursor.execute(sql, [day, exercise, weight, reps])
        
        # Guardamos los cambios en la base de datos
        conn.commit()
        print(f"💪 {exercise.upper()} guardado en {day.upper()}: {weight}kg x {reps} reps.")
        
    except Exception as e:
        print(f"❌ Error al guardar en el gym: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("\n--- 🏋️‍♂️ Aussie Gym: Registro de Carga (PPL) ---")
    d = input("¿Qué día es hoy? (Push/Pull/Legs): ")
    ex = input("Ejercicio: ")
    w = float(input("Peso en kg: "))
    r = int(input("Repeticiones: "))
    
    record_lift(d, ex, w, r)