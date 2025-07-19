students=[]
def add_student():
    name=input("ENTER NAME TO BE ADDED")
    roll=int(input("Enter roll"))
    marks=[]
    while True:

        mark=int(input("Enter marks:"))
        marks.append(mark)
        ch=input("Are you done(y/n)")
        if ch.lower()=='y':
            break
    student_record={"name":name,"roll":roll ,"marks":marks}
    students.append(student_record)
    print(students)
def view_all_students():
    for student in students:
        print("-",student["name"],"Roll Number-",student["roll"])
def display_topper():
    std_name,std_avg=[],[]
    for student in students:
        avg=sum(student["marks"])/len(student["marks"])
        std_name.append(student["name"])
        std_avg.append(avg)
    topper_marks=max(std_avg)
    max_ind=std_avg.index(topper_marks)
    print("Topper is:",std_name[max_ind],topper_marks)
def searchroll():
    sroll=int(input('enter the roll number to be searched'))
    
    for student in students:
        
        if sroll == student["roll"]:
            print(student)
            return
    print("Student not found.")

def disfail():
    for student in students:
        count=0
        for mark in student["marks"]:
            
            if mark<40:
             count+=1
        if count>0:
            print(student,"Has failed in",count,"subjects")
            isfound=True
    if not isfound:
        print("ALL STUDENTS PASSED")
def update_marks():
    notFound=True
    name=input("ENTER NAME TO BE updated")
    for student in students:
        if name==student["name"]:
            while True:
                notFound=False
                print(student["marks"],"which doy ypu want to update")
                udmarks=int(input(":"))
              
                ind=student["marks"].index(udmarks)
                student["marks"][ind]=int(input("Enter the new marks"))
                contd=input("Are you done?(y/n)")
                if contd.lower()=='y':
                
                    break
            print("Updated Marks ",students)
    if notFound:
        print("iNVALID NAME ,pRESS 1 TO ADD THIS STUDENT")
   

            
while True:
    print("\n--- Student Report Card Management System ---")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Display Topper(s)")
    print("4. Search by Roll Number")
    print("5. Display Failed Students")
    print("6. Update Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice == '3':
        display_topper()
    elif choice == '4':
        searchroll()
    elif choice == '5':
        disfail()
    elif choice == '6':
        update_marks()
    elif choice == '7':
        print("Bye bye, see you next exam season! 📚")
        break
    else:
        print("Invalid choice. Try again.")