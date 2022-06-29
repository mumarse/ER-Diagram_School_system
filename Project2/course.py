class Course:
    
    def __init__(self) -> None:
        self.__c_id = None
        self.__c_name = None
        self.__c_credits = None
        # self.course_id = c_id
        # self.course_name = c_name
        # self.course_credits = c_credits
        
    @property
    def course_id(self):
        return self.__c_id
    
    @course_id.setter
    def course_id(self, value):
        self.__c_id = value
            
    @property
    def course_name(self):
        return self.__c_name
    
    @course_name.setter
    def course_name(self, value):
        self.__c_name = value
        
    @property
    def course_credits(self):
        return self.__c_credits
    
    @course_credits.setter
    def course_credits(self, value):
        self.__c_credits = value
    