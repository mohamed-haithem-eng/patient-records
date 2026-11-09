import json
class Patient:
    def __init__(self,name:str,age:int,diagnosis:str):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        
    def __str__(self):
        return f"{self.name} {self.age}  {self.diagnosis}"
    
    def to_dict(self):
        """
        convert obj to dict
        when you write: Patient.to_dict()
        it will return {
        "name":Patient.name, "age":Patient.age, "diagnosis":Patient.diagnosis}
        """

        return {
            "name":self.name,
            "age" :self.age,
            "diagnosis" : self.diagnosis }
    
    @classmethod
    def from_dict(cls, data: dict):
        """   ----EX----
        Patient.from_dict({"name": "jon", "age": 33, "diagnosis": "diabetes"})
        cls  -> Patient
        data -> the dict
        return a new Patient object
        """
        return cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"])

class PatientRegistry:

    def __init__(self):
        self._patients = {}    
        self._id = 1

    def add(self, patient):

        if (not isinstance(patient.name, str) or
            not isinstance(patient.age, int) or
            not isinstance(patient.diagnosis, str)):
            return False
        
        """ ----- duplicate check ----- """
        for p in self._patients.values():
            if p.to_dict() == patient.to_dict():
                return False

        """ ----- create id ----- """
        self._patients[self._id] = patient
        self._id+=1
        return True
    
    def show(self):
        if not self._patients:
            return False

        print("\n","="*10," Patients List ","="*10,sep="")
        for id,p in self._patients.items():
            print("="*10)
            print(f"id: {id}\nname: {p.name}\nage: {p.age}\ndiagnosis: {p.diagnosis}")
        print("="*35)  

    def find(self,id:int):
        return self._patients.get(id, False)

    def remove(self, id):
        if id in self._patients:
            del self._patients[id]
            return True
        return False

    def save(self):
        data = []
        for id,p in self._patients.items():
            d = p.to_dict()
            d["id"] = id
            data.append(d)
        with open("patients.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True     
       
    def load(self):
        try:
            with open("patients.json","r",encoding="utf-8") as file:
                content = file.read().strip()

        except FileNotFoundError:
            return True

        if not content:
            return True
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            return False
        self._patients = {}
        for d in data:
            self._patients[d["id"]] = Patient.from_dict(d)
        self._id = max(self._patients, default=0) + 1
        return True
       
p1 = Patient("mohamed",15,"E")
p2 = Patient("gana",35,"x")

if __name__ == "__main__":
    reg = PatientRegistry()
    if not reg.load():
        print("patients.json is corrupted. Fix or delete it, then run again.")
        raise SystemExit
    reg.add(p1)
    reg.add(p2)
    reg.save()
    reg.load()
    reg.show()