from db_connection import get_connection # <--- Tu conexión segura centralizada

def add_habit_record(name, status, category):
    conn = None
    try:
        # Obtenemos la conexión sin mostrar claves
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # SQL para insertar datos
        sql = "INSERT INTO aussie_habits (habit_name, status, category) VALUES (:1, :2, :3)"
        cursor.execute(sql, [name, status, category])
        
        # ¡Importante! Esto guarda los cambios permanentemente
        conn.commit() 
        print(f"✅ Hábito guardado: {name} ({category})")
        
    except Exception as e:
        print(f"❌ Error al guardar el hábito: {e}")
    finally:
        if conn:
            conn.close()

# --- LÓGICA INTERACTIVA ---
if __name__ == "__main__":
    print("\n--- 🇦🇺 Aussie Tracker: Registro de Hábito ---")
    
    nombre = input("¿Qué hábito completaste? ")
    print("Categorías sugeridas: Physical | Code | English | Money")
    categoria = input("Categoría: ")
    
    if nombre.strip(): 
        # Por defecto el status es "Done"
        add_habit_record(nombre, "Done", categoria)
    else:
        print("⚠️ No escribiste el nombre del hábito, operación cancelada.")