from abc import ABC, abstractmethod
from address import Address

class Person(ABC):
    
    def __init__(self, p_id, p_name, p_cnic) -> None:
        self.__p_id = None
        self.__p_name = None
        self.__p_cnic = None
        self.id = p_id
        self.name = p_name
        self.cnic = p_cnic
        self.full_address = Address()      # composition 
        
    @property
    def id(self):
        pass
    
    @id.setter
    @abstractmethod
    def id(self, value):
        pass
        
    @property
    def name(self):
        pass
    
    @name.setter
    @abstractmethod
    def name(self, value):
        pass
        
    @property
    def cnic(self):
        pass
    
    @cnic.setter
    @abstractmethod
    def cnic(self, value):
        pass