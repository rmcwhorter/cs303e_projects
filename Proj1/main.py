
def take_input(name, lower, upper): # returns int
    val = int(input(f"  Enter {name} grade: "))
    if (val >= lower) and (val <= upper):
        return val 
    else:
        print(f"  Grade must be in range [{lower}..{upper}]. Try again.")
        return take_input(name, lower, upper)

def main():
    name = input("Enter the student's name: ")

    print("HOMEWORKS:")
    hw1 = take_input("HW1", 0, 10)
    hw2 = take_input("HW2", 0, 10)
    hw3 = take_input("HW3", 0, 10)
    print("\nPROJECTS:")
    proj1 = take_input("Project1", 0, 100)
    proj2 = take_input("Project2", 0, 100)

    print("\nEXAMS:")
    ex1 = take_input("Exam1", 0, 100)
    ex2 = take_input("Exam2", 0, 100)

    hw_avg = 10.0 * (hw1 + hw2 + hw3) / 3.0
    proj_avg = (proj1 + proj2) / 2.0
    ex_avg = (ex1 + ex2) / 2.0
    course_avg = (0.3 * hw_avg) + (0.4 * ex_avg) + (0.3 * proj_avg)

    if (course_avg >= 90) and (course_avg <= 100):
        course_letter = "A"
    elif (course_avg >= 80) and (course_avg < 90):
        course_letter = "B"
    elif (course_avg >= 70) and (course_avg < 80):
        course_letter = "C"
    elif (course_avg >= 60) and (course_avg < 70):
        course_letter = "D"
    else: 
        course_letter = "F"

    print(f"\nGrade report for: {name}")
    print(f"  Homework average (30% of grade): {hw_avg}")
    print(f"  Project average (30% of grade): {proj_avg}")
    print(f"  Exam average (40% of grade): {ex_avg}")
    print(f"  Student course average: {course_avg}")
    print(f"  Course grade (CS303E: Spring, 2021): {course_letter}")



    

main()

