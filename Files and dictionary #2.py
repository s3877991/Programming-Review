# FILE AND DICTIONARY EXERCISE:
# Exercise 2: GPA
students = {}

def gpa(marks):
    tot = 0
    for mark in marks:
        tot += mark
    decimal = tot / len(marks) - tot // len(marks)
    if decimal >= 0.5:
        return tot // len(marks) + 1
    return tot // len(marks)


def read_student_info():
    f = open('student.txt', 'r')
    for line in f:
        words = line.split()
        student_id = words[0]
        student_name = ''.join(words[1:])       # nối hai phần tử trong 1 list thành một chuỗi
        students[student_id] = (student_name, [])
    f.close()


def read_student_mark():
    f = open('mark.txt', 'r')
    for line in f:
        words = line.split()
        student_id = words[0]
        marks = int(words[-1])
        students[student_id][1].append(marks)
    f.close()


def display_student_mark():
    for student_id, student_info in students.items():
        print(student_id, student_info[0], gpa(student_info[1]))

read_student_info()
read_student_mark()
display_student_mark()