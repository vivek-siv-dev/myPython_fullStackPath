import os

choices = ["y", "yes", "yup", "offcourse", "defenitly", "sure"]

mainDict = {}
FILE_NAME = "personal_data.txt"


# -----------------------------------------------------
# Utility Functions
# -----------------------------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print(f"\n{'=' * 35} PERSONAL DATA FORM {'=' * 35}")


def save_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for email, details in mainDict.items():
            file.write(f"{email}:{details}\n")


# -----------------------------------------------------
# Add Data
# -----------------------------------------------------

def add_data():
    while True:

        email = input("\nEnter Email : ").strip()

        if email in mainDict:
            print("❌ Email already exists.")
            continue

        subDict = {}

        subDict["name"] = input("Enter Name  : ")
        subDict["age"] = input("Enter Age   : ")
        subDict["city"] = input("Enter City  : ")

        mainDict[email] = subDict

        choice = input("\nAdd another record? : ").lower()

        if choice not in choices:
            break

    save_to_file()

    print("\nData Saved Successfully.")


# -----------------------------------------------------
# View Data
# -----------------------------------------------------

def view_data():

    if not mainDict:
        print("\nNo Records Found.")
        return

    print("\n" + "-" * 70)

    for email, details in mainDict.items():
        print(f"Email : {email}")
        print(f"Name  : {details['name']}")
        print(f"Age   : {details['age']}")
        print(f"City  : {details['city']}")
        print("-" * 70)


# -----------------------------------------------------
# Search
# -----------------------------------------------------

def search_data():

    if not mainDict:
        print("\nDictionary Empty.")
        return

    email = input("\nEnter Email to Search : ")

    if email in mainDict:

        print("\nRecord Found\n")

        print("Email :", email)

        for key, value in mainDict[email].items():
            print(f"{key.title()} : {value}")

    else:
        print("❌ Email Not Found.")


# -----------------------------------------------------
# Update
# -----------------------------------------------------

def update_data():

    if not mainDict:
        print("\nDictionary Empty.")
        return

    while True:

        email = input("\nEnter Email : ")

        if email not in mainDict:
            print("❌ Email Not Found.")
            break

        print("\nAvailable Fields :", list(mainDict[email].keys()))

        field = input("Which field to update : ").lower()

        if field not in mainDict[email]:
            print("❌ Invalid Field.")
            break

        new_value = input("Enter New Value : ")

        mainDict[email][field] = new_value

        save_to_file()

        print("\n✅ Updated Successfully.")

        choice = input("\nUpdate another field? : ").lower()

        if choice not in choices:
            break


# -----------------------------------------------------
# Delete
# -----------------------------------------------------

def delete_data():

    if not mainDict:
        print("\nDictionary Empty.")
        return

    email = input("\nEnter Email to Delete : ")

    if email in mainDict:

        del mainDict[email]

        save_to_file()

        print("✅ Record Deleted.")

    else:
        print("❌ Email Not Found.")


# -----------------------------------------------------
# Main Menu
# -----------------------------------------------------

while True:

    header()

    print("""
1. Add Data
2. Update Data
3. Search Data
4. Delete Data
5. View All Data
6. Exit
""")

    try:
        option = int(input("Select Option : "))

    except ValueError:
        print("❌ Enter Numbers Only.")
        continue

    clear_screen()

    if option == 1:
        header()
        add_data()

    elif option == 2:
        header()
        update_data()

    elif option == 3:
        header()
        search_data()

    elif option == 4:
        header()
        delete_data()

    elif option == 5:
        header()
        view_data()

    elif option == 6:
        print("\nThank You 😊")
        break

    else:
        print("❌ Invalid Choice.")