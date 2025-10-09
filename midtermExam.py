def add_student(gradebook, name, grade):
    if grade > 0 and grade < 100:
        gradebook[name] = grade
        return True
    return False
def get_class_average(gradebook):
    total = 0
    stuAmo = len(gradebook)
    for stu in gradebook:
        total = total + gradebook[stu]
    if total > 0:
        ave = total/stuAmo
        return ave
    else:
        return 0
def get_passing_students(gradebook):
    passing_students = []
    for stu in gradebook:
        if gradebook[stu] >= 60:
            passing_students.append(stu)
    return passing_students

gradebook = {}
print(add_student(gradebook, "Alice",85))
print(add_student(gradebook, "Bob",155))
print(add_student(gradebook, "Chalie",45))
print(get_class_average(gradebook))
print(get_passing_students(gradebook))

###################

def clean_name(name):
    clename = name.strip()
    clename = clename.split(" ")
    clename = clename.lower()
    clename = clename.capitalize()
    clename = clename.join(" ")
    return clename
def validate_email(email):
    valdmail = ""
    try:
        valdmail = email.split("@")
    except:
        print("bad email, try again")
    if valdmail[1].find(".") != -1:
        return True
    else:
        return False
def format_phone(phone):
    formphon = phone.strip()
    if len(formphon) < 10:
        print("Bad number")
        return False
    formphon = formphon.split("-")
    return f"({formphon[0]}) {formphon[1]}-{formphon[2]}"
def process_registration(data_string):
    clendict = {}
    clenStr = data_string.split(",")
    clenStr["name"] = clean_name(clenStr[0])
    clendict["phone"] = format_phone(clenStr[2])
    if validate_email(clenStr[1]):
        clendict["email"] = clenStr[1]
    else:
        print("Try again :p")


print(clean_name(" john smith ")) # Should print "John Smith"
print(validate_email("test@email.com")) # Should print True
print(validate_email("bad.email")) # Should print False
print(format_phone("555-123-4567")) # Should print "(555) 123-4567"
print(format_phone("123")) # Should print "Invalid"
# Test complete processing
test_data = " alice jones ,alice@example.com,9871234567"
print(process_registration(test_data))