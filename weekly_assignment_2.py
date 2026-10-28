
"""
Imagine you are developing an interactive python program for managing the students of your class.
Your task is to create a Python program that interacts with the user to collect and analyze data.
The program should perform the following tasks:

    1. Create an empty dictionary called student_data. Add Information of 10 current ITECH studdents. Each key will be the student's name. Each value will be another dictionary with "age" and "country".

    2.Collect student information manually. Ask the user to enter information for 2 additional students. For each student: Prompt for name, age, and country. Store the information in student_data using the student’s name as the key.
    Allow the user to skip a student by pressing Enter for the name.
    
    3. Calculate the average age of the students. Create a list of ages manually using the dictionary values. Use sum() and len() to calculate the average. Print the average age.
    
    4. Create a set called students_countries to store unique countries.

    7. Create a list called young_students that includes the names of students who are younger than the average age. Print the list of young students.

    8 .Print out the list of young students and the set of unique countries.
    
    9. 
    Extra Challenges (Optional):
    Calculate and print the total number of students. Calculate and print the percentage of students under the average age.


Deliverables:

Submission on Github
Upload on ILIAS

"""

#1 dictionary with 10 ITECH students
student_data = {}
student_data["Carla"] = {"age": 26, "country": "Spain"}
student_data["Lucas"] = {"age": 24, "country": "Germany"}
student_data["Liu"] = {"age": 27, "country": "China"}
student_data["Omar"] = {"age": 29, "country": "Egypt"}
student_data["Sofia"] = {"age": 25, "country": "Italy"}
student_data["Diego"] = {"age": 28, "country": "Mexico"}
student_data["Anita"] = {"age": 26, "country": "India"}
student_data["Jonas"] = {"age": 31, "country": "Germany"}
student_data["Lucia"] = {"age": 23, "country": "Spain"}
student_data["Ema"] = {"age": 30, "country": "Japan"}
print(student_data)

# (3) List of ages, written manually from the dictionary
ages = [
    student_data["Carla"]["age"],
    student_data["Lucas"]["age"],
    student_data["Liu"]["age"],
    student_data["Omar"]["age"],
    student_data["Sofia"]["age"],
    student_data["Diego"]["age"],
    student_data["Anita"]["age"],
    student_data["Jonas"]["age"],
    student_data["Lucia"]["age"],
    student_data["Ema"]["age"],
]

# (4.) Set of unique countries
students_countries = {
    student_data["Carla"]["country"],
    student_data["Lucas"]["country"],
    student_data["Liu"]["country"],
    student_data["Omar"]["country"],
    student_data["Sofia"]["country"],
    student_data["Diego"]["country"],
    student_data["Anita"]["country"],
    student_data["Jonas"]["country"],
    student_data["Lucia"]["country"],
    student_data["Ema"]["country"],
}


#2 Collecting 2 more students from the user (to skip ------> press Enter)
print("\nAdd 2 more students (press Enter to skip)\n")

name1 = input("Name of student 1: ")
if name1 != "":
    age1 = int(input("Age: "))
    country1 = input("Country: ")
    student_data[name1] = {"age": age1, "country": country1}
    ages.append(age1)
    students_countries.add(country1)
else:
    print("Student 1 skipped.")

name2 = input("\nName of student 2: ")
if name2 != "":
    age2 = int(input("Age: "))
    country2 = input("Country: ")
    student_data[name2] = {"age": age2, "country": country2}
    ages.append(age2)
    students_countries.add(country2)
else:
    print("Student 2 skipped.")


#3 average age
average_age = sum(ages) / len(ages)
print(f"\nAverage age: {average_age}")


#7 Students younger than the average
young_students = []
"""
without loop

if student_data["Carla"]["age"] < average_age:
    young_students.append("Carla")
if student_data["Lucas"]["age"] < average_age:
    young_students.append("Lucas")
if student_data["Liu"]["age"] < average_age:
    young_students.append("Liu")
if student_data["Omar"]["age"] < average_age:
    young_students.append("Omar")
if student_data["Sofia"]["age"] < average_age:
    young_students.append("Sofia")
if student_data["Diego"]["age"] < average_age:
    young_students.append("Diego")
if student_data["Anita"]["age"] < average_age:
    young_students.append("Anita")
if student_data["Jonas"]["age"] < average_age:
    young_students.append("Jonas")
if student_data["Lucia"]["age"] < average_age:
    young_students.append("Lucia")
if student_data["Ema"]["age"] < average_age:
    young_students.append("Ema")

#new students only count if they were not skipped
if name1 != "" and age1 < average_age:
    young_students.append(name1)
if name2 != "" and age2 < average_age:
    young_students.append(name2)
"""

#with loop: goes through every key (names)in student_data,so it also includes the students added by the user.
for name in student_data:
    if student_data[name]["age"] < average_age:
        young_students.append(name)

#8 Printing the results
print(f"Young students: {young_students}")
print(f"Unique countries: {sorted(students_countries)}")


#9 Extra
total_students = len(student_data)
percentage_young = len(young_students) / total_students * 100

print(f"\nTotal number of students: {total_students}")
print(f"% of students under the average age: {round(percentage_young, 1)} %")


"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[X] Which ones did you use? (e.g., ChatGPT, Bard, etc.) Claude
[X] Explaining programming concepts
[] Practicing coding exercises
[] Debugging code
[X] Reviewing your Python code
[X] Optimizing code
[] Writing or completing code
[] Other (please specify): _____________

"""  

