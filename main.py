def display_student_summary(names, grades):
    print("\n--- Students Summary ---")
    for i in range(len(names)):
        print(names[i] + ": " + str(grades[i]))