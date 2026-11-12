def grader(grades):
    with open(grades, 'r') as file:
        line = file.readline()
        line_split = grades.split(':')
        name = line_split[0]
        grades = line_split[1]
        grade = 0
        count = 0
        for char in grades: 
            if char == 'A':
                grade += 4.0
            elif char == 'B':
                grade += 3.0
            elif char == 'C':
                grade += 2.0
            elif char == 'D':
                grade += 1.0
            elif char == 'E' or char == 'F':
                grade == 0.0
            count += 1

        grade = grade/count
    with open('completed_grades.txt', 'w') as file2:
        combined = name + grade
        file2.write(combined)

    return file2
    

