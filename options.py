import csv,os # Import csv and os modules

def addContact(*arg): # Procedure addContact
    with open("db.csv","r") as read: # Open db.csv in read-only mode
        reader = csv.reader(read,skipinitialspace=True) # Read as CSV file
        readerList = list(reader) # Convert CSV contents to list
        try: # Attempt to run
            id = int(readerList[len(readerList)-1][0])+1 # Set ID for contact
        except: id = 1 # If error, id set to default 1

    with open("db.csv","a") as write: # Open db.csv in append mode
        writer = csv.writer(write) # Write to as CSV file
        row = [id] # ID as first item in row
        for item in arg: # Each variable passed to function
            row.append(item) # Append to row

        writer.writerow(row) # Write row to database

def deleteContact(id): # Procedure deleteContact taking in ID
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)

    index = findIndex(readerList,id) # Find row with ID
    readerList.pop(index) # Remove row

    with open("db.csv","w") as write: # Open db.csv in write mode
        writer = csv.writer(write)
        writer.writerows(readerList) # Overwrite contents of database

def editContact(id): # Procedure editContact taking in ID
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)
    
    index = findIndex(readerList,id)

    clearScreen() # Clear screen
    print("-------EDIT CONTACT-------")
    print("Leave a field empty to keep the same.")
    readerList[index][1] = input("First name: ") or readerList[index][1] # Ask user for new first name, if left empty will stay the same
    readerList[index][2] = input("Last name: ") or readerList[index][2]
    readerList[index][3] = input("Email: ") or readerList[index][3]
    readerList[index][4] = input("Phone: ") or readerList[index][4]
    readerList[index][5] = input("Address: ") or readerList[index][5]

    with open("db.csv","w") as write:
        writer = csv.writer(write)
        writer.writerows(readerList)

def findIndex(rows,id): # Function findIndex taking in rows (2d array) and ID
    for i in range(0,len(rows)): # Loop i from 0 to length of rows
        if rows[i][0] == str(id): # If item 0 of row i is equal to ID
            return i # Return i; the index has been found
        
def sortContacts(): # Function sortContacts
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)
        readerList = readerList[1:len(readerList)] # Slice out header from readerList
        # This does a bubble sort of readerList in ascending order of names
        for i in range(0,len(readerList)): # Loop i from 0 to length of readerList
            for j in range(0,len(readerList)-i-1): # Loop j from 0 to length of readerList subtract i and 1
                fn1 = f"{readerList[j][1]} {readerList[j][2]}" # Combine first and last names of first row
                fn2 = f"{readerList[j+1][1]} {readerList[j+1][2]}" # Combine first and last names of second row
                if fn1 > fn2: # If full name of first row larger than full name of second row
                    backup = readerList[j] # Backup first row
                    readerList[j] = readerList[j+1] # Set first row to contents of second row
                    readerList[j+1] = backup # Set second row to backed-up contents of first row

    return readerList # Return sorted list

def viewContact(row): # Procedure viewContact taking row
    clearScreen() # Clear screen
    print("-------CONTACT DETAILS-------")
    print(f"First name: {row[1]}")
    print(f"Last name: {row[2]}")
    print(f"Email: {row[3]}")
    print(f"Phone: {row[4]}")
    print(f"Address: {row[5]}")


def clearScreen(): # Procedure clearScreen
    os.system('cls' if os.name == 'nt' else 'clear') # If on Windows, run cls; else run clear