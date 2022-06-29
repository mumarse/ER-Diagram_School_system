from person import Person

class Student(Person):
    
    def __init__(self, p_id=1, p_name='Anas', p_cnic='4213') -> None:
        super().__init__(p_id, p_name, p_cnic)
        self.__cgpa = None
        self.__fee = None
        # self.cgpa = cgpa
        # self.fee = fee
        
    @property
    def cgpa(self):
        return self.__cgpa
    
    @cgpa.setter
    def cgpa(self, value):
        self.__cgpa = value
        
    @property
    def fee(self):
        return self.__fee
    
    @fee.setter
    def fee(self, value):
        self.__fee = value
        
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
        