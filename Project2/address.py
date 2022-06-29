class Address:
    
    def __init__(self, city: str = "Lhr", country: str = "Pak") -> None:
        self.__city = None
        self.__country = None
        self.city = city         
        self.country = country
    
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        if len(value) < 3:
            raise AttributeError("Invalid City Name")
        self.__city = value 
        
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        self.__country = value 