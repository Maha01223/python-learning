
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

"""grade = [86,92,28,90,88]

#add
grade.append(95)

#calculating the average grade.
Average_Grade = sum(grade)/len(grade)
print(f"Average Grade: {Average_Grade: .2f}")


#finding the higest and lowest grade.

higest_grade = max(grade)
print(f"higest Grade: {higest_grade}")
lowest_grade = min(grade)
print(f"lowest  Grade: {lowest_grade}")"""


#Managing An Inventory
#use a list to manage inventory iems in a store.    

"""invenory = ["apple","banana","orange","grapes"]

#adding a new items
invenory.append('strawberies')
print(invenory)

#removing itesm  that iss out of stock.
invenory.remove('banana')
print(invenory)

#checking if an item is in stock

item = "orange"

if item in invenory:
    print(f"{item} are in stock")
else:
    print(f"{item} are out of stock")


#printing the inventory

print("Inventory list:")
for item in invenory:
    print(f"-{item}")"""


#Collecting User Feedback

# use a list to collect and analyze user feedback

feedback= ["grae service","very satisfied","coud be better","excelent experience"]

#adding
feedback.append("Not happy with the services")

#counting specific feedback
posiive_feedback = sum (1 for comment in feedback if "greet" in comment.lower() or "excelent" in comment.lower())

print(f" feedback count: {posiive_feedback}")

#prining all feedback

print("user feedback")
for comment in feedback:
    print(f"-{comment}")