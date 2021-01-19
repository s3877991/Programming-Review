# FILE AND DICTIONARY EXERCISE:
# Exercise 2: GPA
def read_students(file_name):
    f = open(file_name, 'r')
    student = {}
    for line in f:
        words = line.split()
        id = words[0]
        name = words[1]
        surname = words[2]
        print(id, '', name, '', surname)
    f.close()
    return student


def read_mark(file_name):
    f = open(file_name, 'r')
    for line in f:
        words = line.split()
        words = line.split()
        marks = int(words[-1])
    f.close()
    return marks


student_id = read_students('student.txt')
student_mark = read_mark('mark.txt')
print(student_id, student_mark)
