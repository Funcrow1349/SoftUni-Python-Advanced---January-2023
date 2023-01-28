#   Diyan is a student and he wants your help.
#   He wants a program that calculates whether he gets a diploma or not.
#   Write a function students_credits which receives a different number of strings.
#   Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
#   Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets are proportional to
#   his points on the test. For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test
#   points, he will get 12.5 credits for the course.
#   Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's
#   credits.
#   Finally, return a string on multiple lines containing:
#   •	Diyan's achievement message:
#       o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with
#           {total credits} credits."
#       o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
#   •	Information for each course and Diyan's credits:
#       o	"{course name} - {diyan's credits}"
#       o	Note: Each course data should be on a new line.
#   •	All credits must be formatted to the first decimal place.
#   Input
#   •	There will be no input, just any number of strings with courses data passed to your function
#   Output
#   •	The function should return a string in the format described above:
#   Constraints:
#   •	There will always be at least one course.
#   •	There will not be two or more courses with the same name.
#   •	All points and all credits will be whole numbers

def students_credits(*courses):
    credits_for_diploma = 0
    all_courses = {}
    final_message = ""
    for course in courses:
        course_name, course_credits, max_score, current_score = course.split("-")
        percentage = (int(current_score) / int(max_score)) * 100
        current_credits = (percentage / 100) * int(course_credits)
        credits_for_diploma += current_credits
        all_courses[course_name] = current_credits
    if credits_for_diploma >= 240:
        final_message += f"Diyan gets a diploma with {credits_for_diploma:.1f} credits.\n"
    else:
        credits_needed = 240 - credits_for_diploma
        final_message += f"Diyan needs {credits_needed:.1f} credits more for a diploma.\n"
    all_courses = dict(sorted(all_courses.items(), key=lambda x: -x[1]))
    for key, value in all_courses.items():
        final_message += f"{key} - {value:.1f}\n"
    return final_message


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

#   Additional test inputs:
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
#
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
