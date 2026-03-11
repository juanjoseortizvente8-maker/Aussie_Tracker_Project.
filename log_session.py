from db_connection import get_connection # <--- Conexión centralizada y segura

def record_set(day, exercise, weight, reps, set_number):
    conn = None
    try:
        # Obtenemos la conexión desde tu archivo de secretos
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL: Guardamos cada serie como una entrada individual
        sql = """INSERT INTO gym_progress (workout_day, exercise_name, weight_kg, reps, sets) 
                 VALUES (:1, :2, :3, :4, :5)"""
        
        cursor.execute(sql, [day, exercise, weight, reps, set_number])
        conn.commit()
        
    except Exception as e:
        print(f"❌ Error al guardar la serie {set_number}: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("\n--- 🏋️‍♂️ MODO ENTRENAMIENTO GRANULAR ---")
    dia = input("¿Qué rutina hiciste? (Push/Pull/Legs): ")
    
    while True:
        ejer = input("\nEjercicio (o 'exit' para terminar): ")
        if ejer.lower() == 'exit': 
            break
        
        try:
            num_series = int(input(f"¿Cuántas series hiciste de {ejer}?: "))
            
            for i in range(1, num_series + 1):
                peso = float(input(f"  Peso serie {i} (kg): "))
                reps = int(input(f"  Reps serie {i}: "))
                record_set(dia, ejer, peso, reps, i)
                print(f"  ✅ Serie {i} guardada.")
        except ValueError:
            print("⚠️ Por favor, introduce números válidos para series, peso y reps.")

    print("\n🔥 ¡Entrenamiento guardado serie por serie! A descansar, mate. 🇦🇺")