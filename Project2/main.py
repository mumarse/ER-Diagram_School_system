from demodb import DemoDB
from batch import Batch
from student import Student

if __name__ == "__main__":
    
    db = DemoDB()
    db.existing_records()  
    
    while True:
        print("Press 1 for Display Records")
        print("Press 2 for Add new Batch")
        print("Press 3 for Search Student Record")
        print("Press 4 for Exit")
        num = int(input())
        
        if num == 1:
            res = db.display_all_records()
            print(res)
        elif num == 2:
            batch = Batch()
            batch.batch_id = int(input("Enter batch Id: "))
            batch.batch_name = input("Enter batch Name: ")
            batch.course.course_id = int(input("Enter Course Id: "))
            batch.teacher.full_address.city = input("Enter teacher City: ")
            total = int(input("Enter total no of students you want to add: "))
            for i in range(total):
                std = Student()
                std.name = input("Enter Student Name: ")
                std.full_address.city = input("Enter Student City: ")
                batch.students.append(std)
            
            db.add_new_batch(batch)
            
        elif num == 3:
            student_name = input("Enter Student Name for search record : ")
            std_data = db.search_student_record(student_name)
            print(std_data)
        elif num == 4:
            print('Thanks')
            break
        else:
            print("No Action")
        
    