import csv,os

def addContact(*arg):
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)
        try:
            id = int(readerList[len(readerList)-1][0])+1
        except: id = 1

    with open("db.csv","a") as write:
        writer = csv.writer(write)
        entry = [id]
        for item in arg:
            entry.append(item)

        writer.writerow(entry)

def deleteContact(id):
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)

    index = findIndex(readerList,id)
    readerList.pop(index)

    with open("db.csv","w") as write:
        writer = csv.writer(write)
        writer.writerows(readerList)    

def editContact(id):
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)
    
    index = findIndex(readerList,id)

    clearScreen()
    print("-------EDIT CONTACT-------")
    print("Leave a field empty to keep the same.")
    readerList[index][1] = input("First name: ") or readerList[index][1]
    readerList[index][2] = input("Last name: ") or readerList[index][2]
    readerList[index][3] = input("Email: ") or readerList[index][3]
    readerList[index][4] = input("Phone: ") or readerList[index][4]
    readerList[index][5] = input("Address: ") or readerList[index][5]

    with open("db.csv","w") as write:
        writer = csv.writer(write)
        writer.writerows(readerList)

def findIndex(rows,id):
    for i in range(0,len(rows)):
        if rows[i][0] == str(id):
            return i
        
def sortContacts():
    with open("db.csv","r") as read:
        reader = csv.reader(read,skipinitialspace=True)
        readerList = list(reader)
        readerList = readerList[1:len(readerList)]
        for i in range(0,len(readerList)):
            for j in range(0,len(readerList)-i-1):
                fn1 = f"{readerList[j][1]} {readerList[j][2]}"
                fn2 = f"{readerList[j+1][1]} {readerList[j+1][2]}"
                if fn1 > fn2:
                    backup = readerList[j]
                    readerList[j] = readerList[j+1]
                    readerList[j+1] = backup

    return readerList

def viewContact(row):
    clearScreen()
    print("-------CONTACT DETAILS-------")
    print(f"First name: {row[1]}")
    print(f"Last name: {row[2]}")
    print(f"Email: {row[3]}")
    print(f"Phone: {row[4]}")
    print(f"Address: {row[5]}")


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') 