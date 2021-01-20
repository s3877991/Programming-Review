# FILE AND DICTIONARY EXERCISE:
# Exercise 3: Display courses
courses = {}

def read_courses():
    f = open('mark.txt', 'r')
    for line in f:
        words = line.split()
        course_name = ' '.join(words[1:-1])
        if course_name in courses:
            courses[course_name] += 1
        else:
            courses[course_name] = 1
    f.close()


def display_courses():
    for name, enroll in courses.items():
        print(name, enroll)

read_courses()
display_courses()