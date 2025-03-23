import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE contacts 
                  (id INTEGER PRIMARY KEY,
                   name TEXT, 
                   phone INT NOT NULL, 
                   email TEXT)''')
conn.commit()

def add_contact():
    name, phone, email = input("Name: "), input("Phone: "), input("Email: ")
    try:
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        print("Contact added!")
    except sqlite3.IntegrityError:
        print("Phone number already exists!")

def update_contact():
    name = input("Enter name to update: ")
    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    contact=cursor.fetchone()
    if contact():
        new_phone=input(f"New phone number({contact[2]}):") or contact[2]
        new_email=input(f"New Email ({contact[3]}): ") or contact[3]
        cursor.execute("UPDATE contacts SET phone=?, email=?,WHERE name=?",(new_phone, new_email, name))
        conn.commit()
        print("contact updated")
        
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    print("Contact deleted!" if cursor.rowcount else "Contact not found!")

def search_contact():
    query = input("Search by Name or Phone: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%' + query + '%', '%' + query + '%'))
    print(cursor.fetchall() or "No contacts found!")

def view_all():
    cursor.execute("SELECT * FROM contacts")
    print(cursor.fetchall() or "No contacts available!")

menu = {"1": add_contact, "2": update_contact, "3": delete_contact, "4": search_contact, "5": view_all, "6": exit}

while True:
    choice = input("\n1.Add 2.Update 3.Delete 4.Search 5.View 6.Exit\nChoose: ")
    menu.get(choice, lambda: print("Invalid choice!"))()
