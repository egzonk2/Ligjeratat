Has_High_Income = True
Has_Good_Credit = True

if Has_Good_Credit and Has_High_Income:
    print('Eligible for Loan')
else:
    print('Uneligible for loan')

Has_Big_Income = False
Has_Great_Credit = True

if Has_Big_Income or Has_Great_Credit:
    print('Eligible for Loan')
else:
    print('Uneligible for loan')

Has_Amazing_Income = True
Has_Criminal_Record = False

if Has_Amazing_Income and not Has_Criminal_Record:
    print('Eligible for Loan')
else:
    print('Uneligible for loan')
