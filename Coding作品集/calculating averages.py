student_names = ["Alice", "Bob", "Charlie", "Daisy", "Evan"]
student_grades = [85, 58, 73, 62, 45]
total=0
average=0  
letter=''


for i in range(len(student_names)):
    name=student_names[i]
    grade=student_grades[i] 

    if grade<60:
        letter='F'
    elif 60<=grade and grade<70:
        letter='D'
    elif 70<=grade and grade<80:
        letter='C'
    elif 80<=grade and grade<90:
        letter='B'   
    else:
        letter='A'
    print(name,grade,letter)
    total+=grade
    average=total/len(student_grades)

     
print('average=',average) 