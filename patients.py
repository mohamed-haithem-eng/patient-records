patients = []

def add_patient(name, age, diagnosis):
    patient = {
        "name":name,"age": age, "diagnosis":diagnosis
        }
    patients.append(patient)
    
def list_patients():
    print("\n", "="*20 ," patients list:" , len(patients) , "="*20)
    for num,patient in enumerate(patients,start=1):
        print(f"{num}.  name: {patient['name']}")
        print(f"    age: {patient['age']}")
        print(f"    diagnosis: {patient['diagnosis']}")
        print("=" * 40)

if __name__ == "__main__":
    add_patient("Ahmed", 30, "Flu")
    add_patient("Sara", 25, "Migraine")
    add_patient("Omar", 40, "Diabetes")
    list_patients()