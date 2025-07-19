marks={"Nitesh":[99,99,100],
       "Khulal":[23,24,19],
       "Ankit":[12,99,17]
       }
print("Current marks:",marks)
avg_marks=[]
name=[]
for key in marks:
    total=sum(marks[key])
    average=total/3
    avg_marks.append(average)
    name.append(key)
    print(f"Average of {key} is",average)
ind=avg_marks.index(max(avg_marks))
print('THE TOPPER IS ',name[ind])
student = input("\nEnter the name of the student whose marks you want to update: ")
if student in marks :
   udmarks_index=int(input('Enter which subjetct marks you want to change 1/2/3'))-1
   marks[student][udmarks_index]=int(input('Enter new marks'))
print("update marks are",marks)


