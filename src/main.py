from menu import show_menu

def main():
    operations = []
    balance = 0
    print("Welcome to Personal Finance Tracker!")
    balance = show_menu(operations, balance)
    print(f"Final balance: ${balance}")
    print("Thanks for using the app!")

main()
