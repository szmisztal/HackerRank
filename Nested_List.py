python_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    python_students.append([name, score])

def by_grade(element):
    return element[1]

def by_name(element):
    return element[0]

sorted_students = sorted(python_students, key = by_grade)

def find_second_grade(list):
    for student in list:
        i = 0
        if student[1] == list[i][1]:
            pass
        elif student[1] > list[i][1]:
            return student[1]
        i += 1
second_grade = find_second_grade(sorted_students)
for student in sorted(python_students, key = by_name):
    if student[1] == second_grade:
        print(student[0])
