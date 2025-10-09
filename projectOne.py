from datetime import date
ContactsDB = {}

def MakeContact(ContactsDB):
    fName = input(print("Please input the first name of the contact: "))
    lName = input(print("Please input the last name of the contact: "))
    phoneNum = input(print("Please input the phone number of the contact (ex. 123-456-7890): "))
    email = input(print("Please input the Email of the contact: "))
    strt = input(print("Please input the street address of the contact: "))
    city = input(print("Please input the city address of the contact: "))
    stte = input(print("Please input the State address of the contact: "))
    zpcd = input(print("Please input the zip code address of the contact: "))
    cata = input(print("Please input the catagory of the contact (personal, work, family): "))
    notes = input(print("Please input at most a sentence of notes about the contact: "))
    dtemde = date.today()
    
    tryAgain = False
    if fName == "":
        tryAgain = True
    if lName == "":
        tryAgain = True
    if phoneNum == "":
        tryAgain = True

    while tryAgain:
        if fName == "":
             fName = input(print("Please input the first name of the contact: \n"))
             tryAgain = False
        if lName == "":
             lName = input(print("Please input the last name of the contact \n"))
             tryAgain = False
        if phoneNum == "":
             phoneNum = input(print("Please input the phone number of the contact (ex. 123-456-7890) \n"))
             tryAgain = False
        if fName == "":
            tryAgain = True
        if lName == "":
            tryAgain = True
        if phoneNum == "":
            tryAgain = True

    contact = {
        'first_name': fName,
        'last_name': lName,
        'phone': phoneNum,
        'email': email,
        'address': {
            'street': strt,
            'city': city,
            'state': stte,
            'zip_code': zpcd
        },
        'category': cata,
        'notes': notes,
        'created_date': dtemde,
        'last_modified': dtemde
    }
    
    ContactsDB["contact-"+str(len(ContactsDB))] = contact

def display_contact(ContactsDB, ContactID):
    try:
        if ContactsDB[ContactID]:
            Keys = ContactsDB[ContactID].keys()
            for partkeys in Keys:
                if isinstance(ContactsDB[ContactID][partkeys], dict):
                    addKeys = ContactsDB[ContactID][partkeys].keys()
                    for addPrts in addKeys:
                        if ContactsDB[ContactID][partkeys][addPrts] != "":
                            print(f"{addPrts} is {ContactsDB[ContactID][partkeys][addPrts]}")
                else:
                    if ContactsDB[ContactID][partkeys] != "":
                            print(f"{partkeys} is {ContactsDB[ContactID][partkeys]}")
    except KeyError:
        print("That ID doesn't exist")
        return(False)
    except:
        print("An unexpected error occured")

def list_all_contacts(ContactsDB):
    try:   
        for Keys in ContactsDB:
            Keysed = ContactsDB[Keys].keys()
            for partkeys in Keysed:
                if isinstance(ContactsDB[Keys][partkeys], dict):
                    addKeys = ContactsDB[Keys][partkeys].keys()
                    for addPrts in addKeys:
                        if ContactsDB[Keys][partkeys][addPrts] != "":
                            print(f"{addPrts} is {ContactsDB[Keys][partkeys][addPrts]}")
                else:
                    if ContactsDB[Keys][partkeys] != "":
                            print(f"{partkeys} is {ContactsDB[Keys][partkeys]}")
    except:
        print("An unexpected error occured")

def Search_contacts_by_name(ContactsDB, name):
    try:   
        for Keys in ContactsDB:
            Keysed = ContactsDB[Keys].keys()
            if ContactsDB[Keys]['first_name'] == name:
                for partkeys in Keysed:
                    if isinstance(ContactsDB[Keys][partkeys], dict):
                        addKeys = ContactsDB[Keys][partkeys].keys()
                        for addPrts in addKeys:
                            if ContactsDB[Keys][partkeys][addPrts] != "":
                                print(f"{addPrts} is {ContactsDB[Keys][partkeys][addPrts]}")
                    else:
                        if ContactsDB[Keys][partkeys] != "":
                                print(f"{partkeys} is {ContactsDB[Keys][partkeys]}")
    except:
        print("An unexpected error occured")

def Search_contacts_by_category(ContactsDB, cata):
    try:   
        for Keys in ContactsDB:
            Keysed = ContactsDB[Keys].keys()
            if ContactsDB[Keys]['category'] == cata:
                for partkeys in Keysed:
                    if isinstance(ContactsDB[Keys][partkeys], dict):
                        addKeys = ContactsDB[Keys][partkeys].keys()
                        for addPrts in addKeys:
                            if ContactsDB[Keys][partkeys][addPrts] != "":
                                print(f"{addPrts} is {ContactsDB[Keys][partkeys][addPrts]}")
                    else:
                        if ContactsDB[Keys][partkeys] != "":
                                print(f"{partkeys} is {ContactsDB[Keys][partkeys]}")
    except:
        print("An unexpected error occured")

def Search_contacts_by_phone(ContactsDB, phnum):
    try:   
        for Keys in ContactsDB:
            Keysed = ContactsDB[Keys].keys()
            if ContactsDB[Keys]['phone'] == phnum:
                for partkeys in Keysed:
                    if isinstance(ContactsDB[Keys][partkeys], dict):
                        addKeys = ContactsDB[Keys][partkeys].keys()
                        for addPrts in addKeys:
                            if ContactsDB[Keys][partkeys][addPrts] != "":
                                print(f"{addPrts} is {ContactsDB[Keys][partkeys][addPrts]}")
                    else:
                        if ContactsDB[Keys][partkeys] != "":
                                print(f"{partkeys} is {ContactsDB[Keys][partkeys]}")
    except:
        print("An unexpected error occured")

def update_contact(ContactDB, contact_id, field_updates):
    if isinstance(dict, field_updates):
        ContactDB[contact_id].update(field_updates)
        return True
    else:
        print("Update failed, please input a list*")
        return False


def delete_contact(ContactsDB, contact_id):
    try:   
        check = input(print(f"Are you sure you want to delete your contact with {ContactsDB[contact_id]["first_name"]} {ContactsDB[contact_id]["last_name"]}? (Y/N) \n"))
        if check.upper() == 'Y':
            ContactsDB.pop(contact_id)
            print(f"{ContactsDB[contact_id]["first_name"]} {ContactsDB[contact_id]["last_name"]} was deleteded")
            return True
        else:
            print(f"{ContactsDB[contact_id]["first_name"]} {ContactsDB[contact_id]["last_name"]} was not deleteded")
            return False
    except:
        print("An unexpected error occured")

def make_update_dict():
    updict = []
    updating = True
    while updating:
        upda = input(print("What do you need to update? \n1. First name?\n2. Last name?\n3. Phone Number?\n4. Email?\n5. Street?\n6. City?\n7. State?\n8. Zip code?\n9. Category?\n10. Notes?"))
        if upda == "1":
            fName = input(print("Please input the first name of the contact: "))
            updict['first_name'] = fName
        if upda == "2":
            lName = input(print("Please input the last name of the contact: "))
            updict['last_name'] = lName
        if upda == "3":
            phoneNum = input(print("Please input the phone number of the contact (ex. 123-456-7890): "))
            updict['phone'] = phoneNum
        if upda == "4":
            email = input(print("Please input the Email of the contact: "))
            updict['email'] = email
        if upda == "5":
            strt = input(print("Please input the street address of the contact: "))
            updict['street'] = strt
        if upda == "6":
            city = input(print("Please input the city address of the contact: "))
            updict['City'] = city
        if upda == "7":
            stte = input(print("Please input the State address of the contact: "))
            updict['State'] = stte
        if upda == "8":
            zpcd = input(print("Please input the zip code address of the contact: "))
            updict['zip_code'] = zpcd
        if upda == "9":
            cata = input(print("Please input the catagory of the contact (personal, work, family): "))
            updict['category'] = cata
        if upda == "10":
            notes = input(print("Please input at most a sentence of notes about the contact: "))
            updict['notes'] = notes
        updat = input("Do you need to update anything still? (Y/N)")
        if updat.upper() == "N":
            updating = False
    dtemde = date.today()
    updict['last_modified'] = dtemde
    return updict

def main_menu():
    print("Welcome to the Contacts DB, please input what you would like to do")
    continuing = True
    while continuing:
        action = input(print(f"1. Add new contact\n2. Search contacts\n3. List all contacts\n4. Update contact\n5. Delete contact\n6. Exit"))
        if(action == "1"):
            MakeContact()
        if(action == "2"):
            typesearch = input(print("What kind of search? \n1. Name\n2. number\n3. Category"))
            if typesearch == 1:
                name = input(print("What name are you looking for?  "))
                Search_contacts_by_name(ContactsDB, name)
            if typesearch == 2:
                phone = input(print("What phone number are you looking for?  "))
                Search_contacts_by_phone(ContactsDB, phone)
            if typesearch == 3:
                cate = input(print("What category are you looking for?  "))
                Search_contacts_by_category(ContactsDB, cate)
        if(action == "3"):
            list_all_contacts()
        if(action == "4"):
            Contnumb = input("Please input the number of the contact? (number is based on when you initally added it)")
            contact_ID = "contact-"+Contnumb
            updict = make_update_dict()
            update_contact(ContactsDB, contact_ID, updict)
        if(action == "5"):
            Contnumb = input("Please input the number of the contact? (number is based on when you initally added it)")
            contact_ID = "contact-"+Contnumb
            delete_contact(ContactsDB,contact_ID)
        if(action == "6"):
            continuing = False

main_menu()


'''
1. Great job!
2. Grading Rubric:
   * Testing & Documentation--8 out 10
   * Code Quality -- Bonus + 10
   * User Interface -- 15 out of 15
   * Advanced Operations -- 10 out of 35
   * Core Contact Management -- 30 out of 40

   Additional Bonus Points:
        Section 1.3--
                10 points for search_contacts_by_name
                10 points for find_contact_by_pone
3. Total: 93 out of 100.

Keep up the good work!

Dr. X. W.
'''