def grade_reader(grades):
    with open('completed_grades.txt', 'w') as file2:
        pass
    with open(grades, 'r') as file:
        next(file, None)
        for line in file:
            if ':' not in line:
                continue

            line_split = line.split(':', 1)
            name = line_split[0].strip()
            grades = line_split[1].strip()

            grade = 0.0
            count = 0

            for char in grades:
                if char == 'A':
                    grade += 4.0
                    count += 1
                elif char == 'B':
                    grade += 3.0
                    count += 1
                elif char == 'C':
                    grade += 2.0
                    count += 1
                elif char == 'D':
                    grade += 1.0
                    count += 1
                elif char == 'E' or char == 'F':
                    grade += 0.0
                    count += 1

            if count > 0:
                gpa = grade/count
                grade_writer(name, gpa)
    
def grade_writer(name, grade):
    with open('completed_grades.txt', 'a') as file2:
        combined = f'{name}: {grade: .2f}\n'
        file2.write(combined)
