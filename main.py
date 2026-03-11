import os
import random
from datetime import datetime

# --- CONFIGURACIÓN PERSONAL ---
USER_NAME = "JJSK" 
TARGET_DATE = datetime(2027, 1, 1) # Cambia esto a tu fecha estimada de viaje
# ------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_countdown():
    today = datetime.now()
    delta = TARGET_DATE - today
    return delta.days

def get_motivation():
    quotes = [
        "Success is the sum of small efforts, repeated day in and day out.",
        "Your only limit is your mind. Keep pushing!",
        "Australia is waiting for you. Don't stop now!",
        "Consistency is more important than perfection.",
        "Code, lift, save, repeat. That's the way of the Aussie Dev."
    ]
    return random.choice(quotes)

def main():
    while True:
        clear_screen()
        days_left = get_countdown()
        
        print("="*55)
        print(f"👋 G'DAY, {USER_NAME}! Welcome back.")
        print(f"🇦🇺  COUNTDOWN TO AUSTRALIA: {days_left} days left")
        print("="*55)
        print(f"💡 MOTIVATION: {get_motivation()}")
        print("-" * 55)
        print("1. 🏋️‍♂️ GYM: Log PPL Session (Series/Sets)")
        print("2. 📊 GYM: View Training Summary")
        print("3. ✅ HABITS: Log Daily Progress")
        print("4. 📈 HABITS: View Habit Streaks")
        print("5. 💰 MONEY: Add Savings (Soles/Dollars)")
        print("6. 📉 MONEY: View Australia Fund Status")
        print("7. 📂 BACKUP: Export data to CSV (Excel)")
        print("8. ❌ EXIT")
        print("="*55)
        
        choice = input("Select an option (1-8): ")

        if choice == "1":
            os.system('python log_session.py')
        elif choice == "2":
            os.system('python view_session.py')
        elif choice == "3":
            os.system('python log_habit.py')
        elif choice == "4":
            os.system('python view_habits.py')
        elif choice == "5":
            os.system('python log_money.py')
        elif choice == "6":
            os.system('python view_money.py')
        elif choice == "7":
            os.system('python backup_data.py')
        elif choice == "8":
            print(f"\nSee you tomorrow, {USER_NAME}! Catch ya later, mate! 🇦🇺")
            break
        else:
            print("Invalid option. Try again.")
        
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()