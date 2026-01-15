def show_menu():
    print("\nStudent Budget Tracker")
    print("----------------------")
    print("1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "4":
            print("Goodbye!")
            break
        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    main()
