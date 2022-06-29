from teacher import Teacher
from course import Course

class Batch:
    
    def __init__(self) -> None:
        self.__b_id = None
        self.__b_name = None
        self.course = Course()  
        self.teacher = Teacher()
        self.students = []
        
    @property
    def batch_id(self):
        return self.__b_id
    
    @batch_id.setter
    def batch_id(self, value):
        self.__b_id = value
        
    @property
    def batch_name(self):
        return self.__b_name
    
    @batch_name.setter
    def batch_name(self, value):
        self.__b_name = value