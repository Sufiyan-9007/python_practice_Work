while True:
    print("--- String Formatting Menu ---")
    name = input("Enter your name : ")
    
    if name.lower() == 'exit':# This line is written using AI
        print("Exiting the program. Goodbye!")# This line is written using AI
        break
        
    print("Select how you want to format your name:")
    print("1. UPPERCASE")
    print("2. lowercase")
    print("3. Capitalized")
    print("4. Title Case")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    print()
    
    match choice:
        case '1':
            print(f"Formatted Name: {name.upper()}")
        case '2':
            print(f"Formatted Name: {name.lower()}")
        case '3':
            print(f"Formatted Name: {name.capitalize()}")
        case '4':
            print(f"Formatted Name: {name.title()}")
        case '5':
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice! Please select between 1 and 5.\n")
            
    print("-" * 30)
