from patients import add_patient, list_patients, search_patient, delete_patient


def check_name(prompt):
    while True:
        name = input(prompt).lower().strip()
        if not name:
            print("Plz Enter Name")
        else:
            return name


def add():
    name = check_name("Enter name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            if 0 < age < 121:
                break
            else:
                print("\n| Invalid age! Must be integer between 1 and 120 |\n")
        except ValueError:
            print("plz Enter int only")

    diagnosis = check_name("Enter diagnosis: ")
    add_patient(name, age, diagnosis)


def search():
    name = check_name("Enter name: ")
    search_patient(name)


def delete():
    name = check_name("Enter name to delete: ")
    delete_patient(name)


options = {
    "1": ("Add", add),
    "2": ("Search", search),
    "3": ("Delete", delete),
    "4": ("List", list_patients),
}

while True:
    print("\n====|Patient Menu|====")
    for key, (name, func) in options.items():
        print(key, name)
    print("5 Exit")

    choice = input("Enter Num: ").strip()

    if choice not in options and choice != "5":
        print("Plz Enter 1 to 5 only")

    else:
        if choice == "5":
            print("Bye")
            break

        elif choice in options:
            options[choice][1]()  # ex: options[3][delete],() mean run func
