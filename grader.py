def grader(grades):
    with open(grades, 'r') as file:
        line = grades.readline()
        grade = 0
        count = 0
        for char in line: 
            if char == 'A':
                grade += 4
            elif char == 'B':
                grade += 3
            elif char == 'C':
                grade += 2
            elif char == 'D':
                grade += 1
            else:
                grade == 0
            count += 1

        grade = grade/count

    

