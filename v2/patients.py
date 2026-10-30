class Patient:
    def __init__(self,name:str,age:int,diagnosis:str):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        
    def __str__(self):
        return f"\n{'='*40}\nname: {self.name}\nage: {self.age}\ndiagnosis: {self.diagnosis}"
    
    def to_dict(self): # mean convert obj to dict,it dont take any data 
        return {
            "name":self.name,
            "age" :self.age,
            "diagnosis" : self.diagnosis }
    
    @classmethod
    def from_dict(cls,data:dict): # mean convert dict to dbj, cls like self and data mean dict
        return cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"] )
        
patient_one = Patient("hary",58,"VV")

patient_two = Patient("rex",16,"CC")

data = {"name":"jon", "age" : 33, "diagnosis" : "EE"}
patient_three = Patient.from_dict(data)

patients = [patient_one,patient_two,patient_three]

for patient in patients:
    print(patient)
print("="*40)