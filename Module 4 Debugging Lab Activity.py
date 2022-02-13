#Module 4: Lab Activity
#Roxy Villagomez

# All files for this assignment is under this one together!

# 1.BRANCHING


year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else: 
    print ("Far out, that's the future!!")

# 2. Collection


authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s" % author + "died in" + "%s."%date)

# 3. GRADING

# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) 

exam_three = int(input("Input exam grade three: "))
 
grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: 
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")


# 4. PIRATE

#Pirate Debugging

greeting = input("Hello, possible pirate! What's the password? ")
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
        print("Greetings, hater of pirates!")

# 5. TIME(#1)

current_Time = input("What is the current time (in hours 0-23)?")
wait_time = input("How many hours do you want to wait?")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)





# 6. TIME(#2)

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_wait_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
