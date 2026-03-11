import requests
from db_connection import get_connection # <--- Tu corazón de conexión segura

def get_real_exchange_rate():
    try:
        # Llamamos a una API gratuita de tipos de cambio
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Extraemos el valor del Sol (PEN)
        rate = data['rates']['PEN']
        return rate
    except Exception as e:
        # Si falla el internet, usamos un precio de respaldo (puedes ajustarlo)
        print(f"⚠️ No se pudo conectar a la API, usando cambio de respaldo. Error: {e}")
        return 3.75 

def save_money(amount_usd, desc):
    conn = None
    try:
        # Usamos la conexión secreta
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()
        sql = "INSERT INTO australia_fund (amount, description) VALUES (:1, :2)"
        cursor.execute(sql, [amount_usd, desc])
        
        conn.commit()
        print(f"\n✅ ¡Depósito guardado en la DB! +${amount_usd:,.2f} USD")
    except Exception as e:
        print(f"❌ Error al guardar en la base de datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("\n--- 🏦 AUSSIE FUND: CONVERSOR AUTOMÁTICO ---")
    
    # Obtenemos el tipo de cambio real de internet
    tipo_cambio = get_real_exchange_rate()
    print(f"🌍 Tipo de cambio actual: 1 USD = {tipo_cambio} PEN")
    
    try:
        moneda = input("¿Vas a ingresar [S]oles o [D]ólares?: ").upper()
        monto_original = float(input("¿Cuánto dinero es?: "))
        motivo = input("Descripción (ej. Ahorro sueldo, Venta): ")

        if moneda == "S":
            monto_final = monto_original / tipo_cambio
            print(f"💱 Convirtiendo {monto_original} PEN a {monto_final:.2f} USD...")
        else:
            monto_final = monto_original

        save_money(monto_final, motivo)
        
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido para el monto.")