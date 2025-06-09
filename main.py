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
