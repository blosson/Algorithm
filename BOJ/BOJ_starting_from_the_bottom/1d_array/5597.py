students = [int(input()) for _ in range(28)]
numbers = []
for i in range(1, 31):
    numbers.append(i)

absent_students = []
for number in numbers:
    if number not in students:      
        absent_students.append(number)

# absent_students.sort()
for absent_student in absent_students:
    print(absent_student)