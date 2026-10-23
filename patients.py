patients = [
    {"name": "mohamed", "age": 18, "diagnosis": "headache"},
    {"name": "zeto", "age": 46, "diagnosis": "anemia"},
    {"name": "ahmed", "age": 25, "diagnosis": "fever"},
]

print("=" * 30 + " Patients list " + "=" * 30)

for i, patient in enumerate(patients, start=1):
    print(f"{i}.  name: {patient['name']}")
    print(f"    age: {patient['age']}")
    print(f"    diagnosis: {patient['diagnosis']}")
    print("=" * 40)
