def display_student_summary(names, grades):
    print("\n--- Students Summary ---")
    for i in range(len(names)):
        print(names[i] + ": " + str(grades[i]))

def get_avg_grade(grades):
    return sum(grades) / len(grades)


def get_heighest_grade(names, grades):
    max_grade = max(grades)
    index = grades.index(max_grade)
    return names[index], max_grade

def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count

def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count


def analyzer():
    names = []
    grades = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input("Enter name of the student: " + str(i + 1) + ":" )
        while True:
            grade = float(input("Enter grade for " + name + " (out of 100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100. Try again.")    
        names.append(name)
        grades.append(grade)


  




