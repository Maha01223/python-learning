
#Real word usecase of list

#Manage to do List
#Create a to do list to keep track of tasks

"""to_do_list = ["buy Groceries", "clean the house", "pay bills"]

#adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go for a run")
print(to_do_list)

#removing a complete task
to_do_list.remove("clean the house")
print(to_do_list)

#checking if a task is in he list

if "pay bills" in to_do_list:
    print(f"dont forget to pay the utility bills")
print("to_do_list Remaning")
for task in to_do_list:
    print(f" -{task}")"""


# Organizing students Grades
#Create a list to store and calculate average grade for students.

grade = [86,92,28,90,88]

#add
grade.append(95)

#calculating the average grade.
Average_Grade = sum(grade)/len(grade)
print(f"Average Grade: {Average_Grade: .2f}")


#finding the higest and lowest grade.

higest_grade = max(grade)
print(f"higest Grade: {higest_grade}")
lowest_grade = min(grade)
print(f"lowest  Grade: {lowest_grade}")

