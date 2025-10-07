# user = {
#     "name": "Alice",
#     "mark": 25,
# }
# print(user["name"])          
# print(user["mark"])     
student_name = [30]
student_mark = [3]
student_name = input("Enter student's name: ")
print("Name:", student_name)  
student_mark = input("Enter student's mark: ")  
print("Score:", student_mark)   


    
    
def calculate_grades(student_marks):
    grades = {}  # dictionary to store results
    name = {}
    mark = {}
  
        
        # Determine grade based on the grading scale
        if 90 <= mark <= 100:
            grades[student] = "A"
        elif 80 <= mark <= 89:
            grades[student] = "B"
        elif 70 <= mark <= 79:
            grades[student] = "C"
        elif 60 <= mark <= 69:
            grades[student] = "D"
        else:
            grades[student] = "F"
    
    return grades

