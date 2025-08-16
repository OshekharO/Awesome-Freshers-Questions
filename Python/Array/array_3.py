# Define the number of students 
num_students = int(input("Enter the number of students: ")) 
 
# Initialize arrays to store names and marks 
student_names = [] 
student_marks = [] 
 
# Input names and marks 
for i in range(num_students): 
    name = input(f"Enter the name of student {i + 1}: ") 
    marks = float(input(f"Enter the marks for {name}: ")) 
     
    student_names.append(name)  # Add name to names array 
    student_marks.append(marks)  # Add marks to marks array 
 
# Display the names and marks 
print("\nStudent Details:") 
for i in range(num_students): 
    print(f"Name: {student_names[i]}, Marks: {student_marks[i]}") 
