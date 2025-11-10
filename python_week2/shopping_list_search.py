# Interactive Shopping List Search

shopping_list = ["apples", "bread", "milk", "cheese"]

def search_items():
    print("\nWelcome to the Shopping List Search!")
    print("Type 'q' anytime to quit.\n")
    
    item_found = False

    while not item_found:
        item = input("Search for an item in your list: ").strip()
        
        if item.lower() == "q":
            print("Exiting search. Goodbye! 👋")
            break  # Exit the loop if user enters 'q'

        # Case-insensitive search
        if item.lower() in [i.lower() for i in shopping_list]:
            item_found = True
            print(f"✅ {item} is on your shopping list.")
        else:
            print(f"❌ {item} is not on your list. Try again.")

# Main loop to allow replay
while True:
    search_items()
    replay = input("\nDo you want to search again? (yes/no): ").strip().lower()
    if replay not in ["yes", "y"]:
        print("\nThanks for using the shopping list search! 👋")
        break
