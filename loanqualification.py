print('Rate from 1 to 10 the following questions where 1 is the lowest and 10 the highest.')
print()
loan = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))
loan_qualification = ""

if loan >= 5:
    if credit >= 7 and income >= 7:
        loan_qualification = True

    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            loan_qualification = True
        else:
            loan_qualification = False

    else:
        loan_qualification = False

else:  # loan < 5:
    if credit < 4:
        loan_qualification = False

    else:
        if income >= 7 or down_payment >= 7:
            loan_qualification = True

        elif income >= 4 and down_payment >= 4:
            loan_qualification = True

        else:
            loan_qualification = False

if loan_qualification:
    print('You are qualified!')

if not loan_qualification: #else:
    print('You are not qualified.')
