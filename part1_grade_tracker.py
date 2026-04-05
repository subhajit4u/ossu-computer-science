# PART 1 : Student Grade Tracker

# Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": "Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"}
]

clean_students = []

print("\n---- CLEANED STUDENT PROFILES ----")

# loop through students and clean data
for s in raw_students:

    # remove extra spaces and convert to title case
    name = s["name"].strip().title()

    # convert roll number to integer
    roll = int(s["roll"])

    # convert marks string to list of integers
    marks = [int(m.strip()) for m in s["marks_str"].split(",")]

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    clean_students.append(student)

    # check if name contains only alphabets
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    print("\n=================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")

    if valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")


# print special formatting for roll number 103
for s in clean_students:
    if s["roll"] == 103:
        print("\nName formats for Roll 103:")
        print("UPPER:", s["name"].upper())
        print("LOWER:", s["name"].lower())



# Task 2 — Marks Analysis

print("\n---- SUBJECT MARKS ANALYSIS ----")

student_name = "Ayesha Sharma"

subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# print subject, marks and grade
for i in range(len(subjects)):

    m = marks[i]

    if m >= 90:
        grade = "A"
    elif m >= 75:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"{subjects[i]} : {m} -> Grade {grade}")


# while loop for adding new subjects
new_subjects = 0

while True:

    subject = input("\nEnter subject name (type 'done' to stop): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # validation for numeric input
    if not mark_input.isdigit():
        print("Invalid marks input")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100")
        continue

    subjects.append(subject)
    marks.append(mark)

    new_subjects += 1

# calculate updated average
avg = sum(marks) / len(marks)

print("\nNew subjects added:", new_subjects)
print("Updated average:", round(avg, 2))


# Task 3 — Class Performance Summary


print("\n---- CLASS PERFORMANCE REPORT ----")

class_data = [
    ("Ayesha Sharma", [88,72,95,60,78]),
    ("Rohit Verma", [55,68,49,72,61]),
    ("Priya Nair", [91,85,88,94,79]),
    ("Karan Mehta", [40,55,38,62,50]),
    ("Sneha Pillai", [75,80,70,68,85])
]

print("\nName | Average | Status")
print("------------------------------")

pass_count = 0
fail_count = 0

top_name = ""
top_avg = 0

total_avg = 0

for name, marks in class_data:

    avg = sum(marks) / len(marks)
    avg = round(avg,2)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    print(f"{name} | {avg} | {status}")

    if avg > top_avg:
        top_avg = avg
        top_name = name

    total_avg += avg


class_average = total_avg / len(class_data)

print("\nStudents Passed:", pass_count)
print("Students Failed:", fail_count)

print("Class Topper:", top_name, "-", top_avg)

print("Class Average:", round(class_average,2))



# Task 4 — String Manipulation Utility


print("\n---- STRING MANIPULATION ----")

essay = "  python is a versatile language. it supports object oriented programming. python is easy to learn. python is powerful.  "

# strip
clean_essay = essay.strip()

# title case
print("\nTitle Case Essay:")
print(clean_essay.title())

# count occurrences
count = clean_essay.lower().count("python")

print("\nWord 'python' appears:", count, "times")

# replace python with emoji version
replaced = clean_essay.replace("python","Python 🐍")

print("\nReplaced Essay:")
print(replaced)

# split sentences
sentences = clean_essay.split(". ")

print("\nSentence List:")
print(sentences)

print("\nNumbered Sentences")

for i, sentence in enumerate(sentences,1):

    if not sentence.endswith("."):
        sentence = sentence + "."

    print(f"{i}. {sentence}")