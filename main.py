import os # Import os module
from options import * # Import everything from options

if not os.path.exists("db.csv") or os.path.getsize("db.csv") == 0: # If db.csv either does not exist or its file size is 0 (empty)
    with open("db.csv","a+") as write: # Open it in append mode as write
        writer = csv.writer(write) # Write to as CSV
        writer.writerow(["Id","FirstName","LastName","Email","Phone","Address"]) # Write header to file

while True: # While loop; repeat until break
    clearScreen() # Clear screen
    print('''
----------CONTACTS----------
1. Add new contact
2. View contact
3. Edit contact
4. Delete contact
5. Exit''') # Present user-friendly options menu
          
    try: # Attempt to execute code
        choice = int(input("Enter a choice: ")) # Ask user for choice and convert it to integer
    except: # If an error occurs running try code, likely due to a non-integer item being entered
        print("Invalid choice, please try again.") # Inform the user
        input("Press enter to continue...") # Wait for enter to be pressed
        continue # Restart loop

    if choice == 1: # If choice is 1 (add contact)
        clearScreen()
        print("--------ADD CONTACT--------")
        # Prompt user for information, storing it as "blank" if left empty
        firstName = input("First name: ") or 'blank'
        lastName = input("Last name: ") or 'blank'
        email = input("Email: ") or 'blank'
        phone = input("Phone: ") or 'blank'
        address = input("Address: ") or 'blank'

        addContact(firstName,lastName,email,phone,address) # Add contact with given data   

    elif choice == 2: # Otherwise, if choice is 2 (view contact)
        rows = sortContacts() # Sort contacts in ascending order based on their full name (first and last)

        while True:
            clearScreen()
            print("-------VIEW CONTACT-------")
            count = 1 # Count will number each row
            for row in rows: # Go through each row
                print(f"{count}. {row[1]} {row[2]}") # Print count along with first and last names
                count += 1 # Increment count

            print(f"{count}. Back") # Count's last value can be entered to go back

            try:
                choice = int(input("Enter a choice: "))
            except:
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            if choice < 1 or choice > count: # If choice is less than 1 or more than count
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            break
        
        if choice != count: # If choice is less than count, so it is a number of a row
            viewContact(rows[choice-1]) # View information in that row
            input("Press enter to continue...") # Display information until user presses enter

    elif choice == 3: # Otherwise, if choice is 3 (edit contact)
        rows = sortContacts()

        while True:
            clearScreen()
            print("-------EDIT CONTACT-------")
            count = 1
            for row in rows:
                print(f"{count}. {row[1]} {row[2]}")
                count += 1

            print(f"{count}. Back")

            try:
                choice = int(input("Enter a choice: "))
            except:
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            if choice < 1 or choice > count:
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            break

        if choice != count:
            id = int(rows[choice-1][0]) # Get ID from column 1 of chosen row
            editContact(id) # Edit contact with that ID

    elif choice == 4: # Otherwise, if choice is 4 (delete contact)
        rows = sortContacts()
        while True:
            clearScreen()
            print("-------DELETE CONTACT-------")
            count = 1
            for row in rows:
                print(f"{count}. {row[1]} {row[2]}")
                count += 1

            print(f"{count}. Back")

            try:
                choice = int(input("Enter a choice: "))
            except:
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            if choice < 1 or choice > count:
                print("Invalid choice, please try again.")
                input("Press enter to continue...")
                continue

            break

        if choice != count:
            id = int(rows[choice-1][0])
            deleteContact(id) # Delete contact with that ID        

    elif choice == 5: # Otherwise, if choice is 5
        break # Break out of loop

    else: # Otherwise, so none of the other if statements were satisfied
        print("Invalid choice, please try again.") # Inform user choice is invalid
        input("Press enter to continue...")
        continue # Restart loop
