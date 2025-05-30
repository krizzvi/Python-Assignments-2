import csv

def import_marks():
    students = []
    with open("marks.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            name, mark = row
            students.append((name, int(mark)))
    return students

def assign_grades(students):
    for name, mark in students:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        else:
            grade = "F"
        print(f"{name}: {mark} - Grade {grade}")

def main():
    students = import_marks()
    assign_grades(students)

if __name__ == "__main__":
    main()