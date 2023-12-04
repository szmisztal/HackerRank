n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()


if query_name in student_marks:
    result = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f'{result:.2f}')

