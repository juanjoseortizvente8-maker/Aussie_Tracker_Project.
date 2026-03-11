from db_connection import get_connection # <--- Centralizamos la seguridad
import oracledb

def reset_tables():
    conn = None
    try:
        # Obtenemos la conexión sin exponer credenciales
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # Lista de tablas a vaciar
        tables = ["gym_progress", "australia_fund", "daily_habits"]
        
        print("\n--- 🧹 INICIANDO LIMPIEZA DE BASE DE DATOS ---")
        
        for table in tables:
            try:
                # TRUNCATE es más rápido y resetea los contadores de ID
                cursor.execute(f"TRUNCATE TABLE {table}")
                print(f"✅ Tabla '{table}' vaciada y reseteada.")
            except Exception as e:
                print(f"⚠️ No se pudo limpiar '{table}': {e}")
        
        # En Oracle, TRUNCATE es DDL y hace commit automático, 
        # pero mantenemos la buena práctica.
        conn.commit()
        print("\n✨ ¡Base de datos impecable! Lista para tus records reales.")
        
    except Exception as e:
        print(f"❌ Error durante el reseteo: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("❗ ADVERTENCIA: Esta acción eliminará TODOS los registros.")
    confirmacion = input("¿Estás seguro de que quieres borrar los datos de prueba? (s/n): ")
    
    if confirmacion.lower() == 's':
        reset_tables()
    else:
        print("Operación cancelada. Los datos están a salvo.")