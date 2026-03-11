import os
from datetime import datetime
from db_connection import get_connection # <--- Tu nueva conexión segura

def show_australia_progress(goal=10000):
    conn = None
    try:
        # Obtenemos la conexión sin revelar la contraseña
        conn = get_connection()
        if conn is None:
            return
            
        cursor = conn.cursor()
        
        # 1. Primero vemos los últimos 5 movimientos para motivarnos
        print(f"\n📜 ÚLTIMOS MOVIMIENTOS:")
        print(f"{'-'*45}")
        sql_history = "SELECT entry_date, amount, description FROM australia_fund ORDER BY entry_date DESC"
        
        cursor.execute(sql_history)
        rows = cursor.fetchmany(5)
        for row in rows:
            fecha = row[0].strftime("%d-%m")
            print(f"📅 {fecha} | +${row[1]:>8.2f} | {row[2]}")
        
        # 2. Sumamos todo para el dashboard
        cursor.execute("SELECT SUM(amount) FROM australia_fund")
        result = cursor.fetchone()[0]
        total_saved = result if result else 0
        
        remaining = goal - total_saved
        percent = (total_saved / goal) * 100
        
        print(f"\n{'='*45}")
        print(f"🇦🇺  ESTADO DEL SUEÑO AUSTRALIANO  🇦🇺")
        print(f"{'='*45}")
        print(f"💰 Llevas:      ${total_saved:,.2f}")
        print(f"🎯 Meta:        ${goal:,.2f}")
        print(f"📉 Faltan:      ${remaining:,.2f}")
        print(f"{'-'*45}")
        
        # Barra de progreso visual
        bar_length = 20
        filled = int(round(bar_length * total_saved / goal))
        bar = '█' * filled + '-' * (bar_length - filled)
        print(f"🚀 PROGRESO: [{bar}] {percent:.2f}%")
        print(f"{'='*45}")

    except Exception as e:
        print(f"❌ Error al leer el fondo: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Puedes ajustar tu meta aquí (ej. 12000 si suben los pasajes)
    show_australia_progress(10000)