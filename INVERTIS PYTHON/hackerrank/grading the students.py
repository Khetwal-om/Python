def grade():
    marks=int(input("Enter the number of grades"))
    quotient=marks//5
    print(quotient)
    if marks<38:
        print("failing grade so we can't do anything")
    else:
        if marks%5>=3:
            marks=quotient*5+5
            print('si')
        else:
            pass


    return marks



print(grade())




'''

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    answer=[]
    for i in grades:
        quotient=i//5
        print(quotient)
        if i<38:
            answer.append(i)
        else:
            if i%5>=3:
                i=quotient*5+5
                answer.append(i)
            else:
                answer.append(i)
    return answer


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()




'''
