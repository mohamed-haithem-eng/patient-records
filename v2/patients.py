class Patient:
    def __init__(self,name:str,age:int,diagnosis:str):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        
    def __str__(self):
        return f"\n{'='*40}\nname: {self.name}\nage: {self.age}\ndiagnosis: {self.diagnosis}"
    
    def to_dict(self): # convert obj to dict,it dont take any data 
        return {
            "name":self.name,
            "age" :self.age,
            "diagnosis" : self.diagnosis }
    
    @classmethod
    def from_dict(cls,data:dict): # convert dict to obj,cls mean class like and data mean dict
        return cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"] )
