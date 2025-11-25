def read_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the name and try again.")

# Run the function
read_file()
