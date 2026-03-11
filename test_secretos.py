from db_connection import get_connection

conn = get_connection()
if conn:
    print("✅ ¡Conexión exitosa! Los secretos funcionan perfectamente.")
    conn.close()
else:
    print("❌ Algo falló. Revisa que tu archivo .env tenga los datos correctos.")