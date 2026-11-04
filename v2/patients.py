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
                return False

        """ create id  and append to list """
        data["id"] = self._id    # ex patient.id = 1
        self._id += 1            # ex self._patient = 2
        self._patients.append(data)
        return True
    
    def show(self):
        if not self._patients:
            print("list is empty")
            return False
        for p in self._patients:
            id = p["id"]
            name=p["name"]
            age=p["age"]
            diagnosis = p["diagnosis"]
            print("="*30)
            print(f"id: {id}\nname: {name}\nage: {age}\ndiagnosis: {diagnosis}")
        print("="*30)  

    def find(self):
        ...
    
    def remove(self):
        ...

    def save(self):
        ...
    
    
p1 = Patient("mohamed",15,"E")
p2 = Patient("gana",35,"x")

reg = PatientRegistry()
reg.add(p1)
reg.add(p2)
reg.show()

