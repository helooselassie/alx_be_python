# Function to display the menu options
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to handle the shopping list
def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nShopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
