from patients import add_patient,list_patients,search_patient,delete_patient

def add():
    name = input("Enter Name: ").lower()
    age  = int(input("Enter Age"))
    diagnosis  = input("Enter Diagnosis").lower()
    add_patient(name,age,diagnosis)

def search():
    search_patient(input("Name to Search: "))

def delete():
    delete_patient(input("Name to Delete: "))
    
options = {
    "1": ("Add",add),
    "2": ("Search",search),
    "3": ("Delete",delete),
    "4": ("List",list_patients)}

while True:
    print("\n====|Patient Menu|====")
    for key,(name,func) in options.items():
        print(key,name)
    print("5 Exit")
    
    choice = input("Enter Num: ")
    
    if choice == 5:
        print("Bye")
        break
    elif choice in options:
        options[choice][1]()
    else:
        print("Invalid choice")