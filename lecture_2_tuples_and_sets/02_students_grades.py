# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a
# student's name and grade. For each student print all his/her grades and finally his/her average grade, formatted to
# the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

number_of_students = int(input())
grades = {}
for entry in range(number_of_students):
    name, grade = input().split()
    if name not in grades:
        grades[name] = []
    grades[name].append(float(grade))

for student, score in grades.items():
    average_score = sum(score) / len(score)
    string_of_grades = ' '.join(map(lambda current_grade: f'{current_grade:.2f}', score))
    print(f"{student} -> {string_of_grades} (avg: {average_score:.2f})")
