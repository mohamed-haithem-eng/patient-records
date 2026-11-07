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
        self._patients = []      
        self._id = 1

    def add(self, patient):
        data = patient.to_dict()

        """ ----- type check ----- """
        if (
            not isinstance(data["name"],str) or
            not isinstance(data["age"],int) or
            not isinstance(data["diagnosis"],str)):
            return False
        
        """ ----- storage chesck ----- """
        for p in self._patients:
            if (p["name"],p["age"],p["diagnosis"]) == (data["name"],data["age"],data["diagnosis"]):
                print("\nyou've repeated this patient\nI'll take first one or in the memory")
                return False

        """ create id  and append to list """
        data["id"] = self._id    # ex patient.id = 1
        self._id += 1            # ex self._patient = 2
        self._patients.append(data)
        return True
    
    def show(self):
        if not self._patients:
            print("\nlist is empty")
            return False
        print("\n","="*10," Patients List ","="*10,sep="")
        for p in self._patients:
            id = p["id"]
            name=p["name"]
            age=p["age"]
            diagnosis = p["diagnosis"]
            print("="*10)
            print(f"id: {id}\nname: {name}\nage: {age}\ndiagnosis: {diagnosis}")
        print("="*35)  

    def find(self,id:int):
        """
        loop in self._patient
        if id in list ,init variables then print
        else exit with warning message """
        
        for p in self._patients:
            if id == p["id"]:
                id = p["id"]
                name=p["name"]
                age=p["age"]
                diagnosis = p["diagnosis"]

                print("\n","="*12," Find it ","="*14,sep="")
                print(f"id: {id}\nname: {name}\nage: {age}\ndiagnosis: {diagnosis}")       
                return p
        
        print("="*35)
        print(f"\nID {id} is not found,I cant search it\n")
        print("="*35)
        return False

    def remove(self,id):
        for p in self._patients:
            if id == p["id"]:
                self._patients.remove(p)
                return True
        print(f"\nID {id} is not found,I cant remove it")
        return False

    def save(self):
        if self._patients:
            with open("patients.json","w",encoding="utf-8") as file:
                json.dump(self._patients,file,ensure_ascii=False,indent=4)
        else:
            print("\nlist empty,u can use add")
            return False

    def load(self):
        try:
            with open("patients.json","r",encoding="utf-8") as file:
                content = file.read().strip()
                if content:
                    self._patients.extend(json.loads(content))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("patients.json is corrupted. Fix or delete it, then run again.")
            raise SystemExit
    
p1 = Patient("mohamed",15,"E")
p2 = Patient("gana",35,"x")

reg = PatientRegistry()
reg.add(p1)
reg.add(p2)
reg.save()