import csv,os
from options import *

if not os.path.exists("db.csv") or os.path.getsize("db.csv") == 0:
    with open("db.csv","a+") as write:
        writer = csv.writer(write)
        writer.writerow(["Id","FirstName","LastName","Email","Phone","Address"])

while True:
    clearScreen()
    print('''
----------CONTACTS----------
1. Add new contact
2. View contact
3. Edit contact
4. Delete contact
5. Exit''')
          
    try:
        choice = int(input("Enter a choice: "))
    except:
        print("Invalid choice, please try again.")
        input("Press enter to continue...")
        continue

    if choice == 1:
        clearScreen()
        print("--------ADD CONTACT--------")
        firstName = input("First name: ") or 'blank'
        lastName = input("Last name: ") or 'blank'
        email = input("Email: ") or 'blank'
        phone = input("Phone: ") or 'blank'
        address = input("Address: ") or 'blank'

        addContact(firstName,lastName,email,phone,address)        

    elif choice == 2:
        rows = sortContacts()

        while True:
            clearScreen()
            print("-------VIEW CONTACT-------")
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

            break
        
        if choice != count:
            viewContact(rows[choice-1])
            input("Press enter to continue...")

    elif choice == 3:
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
            id = int(rows[choice-1][0])
            editContact(id)

    elif choice == 4:
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
            id = int(rows[choice-1][0])
            deleteContact(id)        

    elif choice == 5:
        break

    else:
        print("Invalid choice, please try again.")
        input("Press enter to continue...")
        continue
