# user = {
#     "name": "Alice",
#     "mark": 25,
# }
# print(user["name"])          
# print(user["mark"])     
student_name = [30]
student_mark = [3]
student_name = input("Enter student's name: ")
print("Hello,", student_name)  
student_mark = input("Enter student's mark: ")  
print("Hello,", student_mark)   


for key, value in student_mark.items():
    print(f"{key}:{value}")
    
    
def user_info(name, age):   
    print(f"{name} is {age} years old") 
user_info(age=25, name="ALice")

num = 10
if num >= 20:
    if num < 30:
        print ("NUmber is between 20 and 29")
    else:
        print("number is 30 or greater")
else:
    print("Number is less than 20")