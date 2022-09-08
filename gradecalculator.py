grade_percentage = int(input('What is your grade percentage? '))
if grade_percentage >= 90:
    letter = 'A'
    #print('You got an A! Congratulations! You have passed the class.')
elif grade_percentage >= 80:
    letter = 'B'
    #print('You got a B. Congratulations! You have passed the class.')
elif grade_percentage >= 70:
    letter = 'C'
   #print('You got a C. Congratulations! You have passed the class.')
elif grade_percentage >= 60:
    letter = 'D'
    #print('You got a D. You have not passed the class. Work harder next time!')
else:
    letter = 'F'
    #print('You got a F. You have not passed the class. Work harder next time!')

print()
sign = ''
last_digit = grade_percentage % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
print(f'Your Grade is {letter}{sign}')

print()
if grade_percentage >= 70:
    print('Congratulations! You have passed the class.')
else:
    print('You have not passed the class. Work harder next time!')
