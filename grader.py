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
    with open('completed_grades.txt', 'w') as file2:
        if grade < 1:
            file2.write('F')
        elif grade < 2:
            file2.write('D')
        elif grade < 3:
            file2.write('C')
        elif grade < 4:
            file2.write('B')
        else:
            file2.write('A')


    return file2
    

