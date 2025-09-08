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
    #try:   
        for Keys in ContactsDB:
            for contKeys in ContactsDB[Keys]:
                for partkeys in ContactsDB[Keys][contKeys]:
                    if isinstance(ContactsDB[Keys][contKeys][partkeys], dict):
                        addKeys = ContactsDB[Keys][contKeys][partkeys].keys()
                        for addPrts in addKeys:
                            if ContactsDB[Keys][contKeys][partkeys][addPrts] != "":
                                print(f"{addPrts} is {ContactsDB[Keys][contKeys][partkeys][addPrts]}")
                    else:
                        if ContactsDB[partkeys] != "":
                                print(f"{partkeys} is {ContactsDB[Keys][contKeys][partkeys]}")
    #except:
    #    print("An unexpected error occured")



MakeContact(ContactsDB)
list_all_contacts(ContactsDB)

