from person import Person

class Teacher(Person):
    
    def __init__(self, p_id=1, p_name="Ali", p_cnic="34242") -> None:
        super().__init__(p_id, p_name, p_cnic)
        self.__salary = None
        # self.salary = salary
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value
        
    @property
    def id(self):
        return self.__p_id
    
    @id.setter
    def id(self, value):
        self.__p_id = value 
        
    @property
    def name(self):
        return self.__p_name
    
    @name.setter
    def name(self, value):
        self.__p_name = value 
        
    @property
    def cnic(self):
        return self.__p_cnic
    
    @cnic.setter
    def cnic(self, value):
        self.__p_cnic = value 
        