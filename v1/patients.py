patients = []

def add_patient(name, age, diagnosis):
    patient = {"name": name, "age": age, "diagnosis": diagnosis}
    patients.append(patient)
    
def list_patients():
    print("\n", "=" * 20, " patients list:", len(patients), "=" * 20)
    for num, patient in enumerate(patients, start=1):
        print(f"{num}.  name: {patient['name']}")
        print(f"    age: {patient['age']}")
        print(f"    diagnosis: {patient['diagnosis']}")
        print("=" * 60)

def find(name):
    return [patient for patient in  patients if patient["name"].lower() == name.lower()]
    
def search_patient(name):
    same_patient = find(name)

    if not same_patient:
        print("\n| I couldn't find it |\n")
        return

    for num, patient in enumerate(same_patient, start=1):
        print("=" * 30)
        print(num, patient["name"], "\nage:", patient["age"], " diagnosis:", patient["diagnosis"])

    print("=" * 30)

def delete_patient(name):
    matches = find(name)
    
    if not matches :
        print("\n|I couldn't find it|\n")
        return
    for patient in matches:
        patients.remove(patient)
        
    print(f"Deleted patient: {name}")
