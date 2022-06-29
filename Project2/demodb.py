from batch import Batch
from student import Student

class DemoDB:
    
    def __init__(self) -> None:
        self.__batches = []          
        
    def existing_records(self):
        # 1st Batch
        batch1 = Batch()
        # batchh info
        batch1.batch_id = 101          # set prop            
        batch1.batch_name = "AI-2022"  
        # course info
        batch1.course.course_id = 1001
        batch1.course.course_name = 'AI'
        batch1.course.course_credits = 4
        # teacher info
        batch1.teacher.id = 1
        batch1.teacher.name = "Anas"
        batch1.teacher.cnic = "1010-000000-1"
        batch1.teacher.salary = 232451
        batch1.teacher.full_address.city = "Lahore"
        batch1.teacher.full_address.country = "Pakistan"
        # student information
        # 1st student info
        std1 = Student()
        std1.id = 'AI-1'
        std1.name = "Asad"
        std1.cnic = "3424242"
        std1.cgpa = 3.68
        std1.fee = 42341313
        std1.full_address.city = "Fsd"
        std1.full_address.country = "Turkey"
        batch1.students.append(std1)
        std2 = Student()
        std2.id = 'AI-2'
        std2.name = "Waan"
        std2.cnic = "2341"
        std2.cgpa = 3.6
        std2.fee = 5242
        std2.full_address.city = "Isd"
        std2.full_address.country = "China"
        batch1.students.append(std2)
        
        self.__batches.append(batch1)   # Batch 1

    def display_all_records(self):
        
        records = ""
        batch_len = len(self.__batches)
        for i in range(batch_len):
            records += "*** Batch Info ***\n"
            records += "Batch Id: " + str(self.__batches[i].batch_id) + "\n"
            records += "Batch Name: " + str(self.__batches[i].batch_name) + "\n"
            
            records += "** Course Info **\n"
            records += "Course Id : " + str(self.__batches[i].course.course_id) + "\n"
            # records += "Course Name : " + self.__batches[i].course.course_name + "\n"
            # records += "Course Credits : " + str(self.__batches[i].course.course_credits) + "\n"
            
            records += "** Teacher Info **\n"
            records += "Teacher City : " + self.__batches[i].teacher.full_address.city + "\n"
            
            records += "Student Info \n"
            for j in range(len(self.__batches[i].students)):
                records += "Student Name: " + self.__batches[i].students[j].name + "\n"
                records += "Student City: " + self.__batches[i].students[j].full_address.city + "\n"
                
        return records

    
    def add_new_batch(self, new_batch):
        self.__batches.append(new_batch)   # Batch 2, 3, 4, 
    
    def search_student_record(self, std_name):
        
        records = ""
        batch_len = len(self.__batches)
        for i in range(batch_len):
            records += "*** Batch Info ***\n"
            records += "Batch Name: " + str(self.__batches[i].batch_name) + "\n"
            records += "** Course Info **\n"
            records += "Course Id : " + str(self.__batches[i].course.course_id) + "\n"
            records += "Student Info \n"
            for j in range(len(self.__batches[i].students)):
                if std_name.lower() == self.__batches[i].students[j].name.lower():
                    records += "Student Name: " + self.__batches[i].students[j].name + "\n"
                    records += "Student City: " + self.__batches[i].students[j].full_address.city + "\n"
                    records += "Happy:)"
                    break
            else:
                records += "Sorry :("
                
        return records
