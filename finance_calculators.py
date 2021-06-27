import math

# asking user which calculation they would like to do
print('''Choose either 'investment' or 'bond' from the menu below:

investment      - to calculate the amount of interest you'll earn on interest
bond            - to calculate the amount you'll have to pay on a home loan
''')

# storing users calculation type into a variable: investment or bond
calculation = input("What would you like to calculate: ").lower()

# variables to keep in mind for investment
paid_amount = 0
final_amount = 0
interest_rate = 0   # percentage
years = 0
interest = ""       # simple or compound

# variables to keep in mind for bond
present_value = 0           # current value of house
interest_rate = 0           # percentage
repay_time = 0              # months to repay loan

# asking user for relevent information to do the calculation(eg. interest rate,number of years)and then storing it in a variable
if calculation == "investment":
    paid_amount = float(input("Deposit amount(R): "))
    interest_rate = float(input("Interest rate(%): "))
    years = float(input("Amount of years: "))
    interest = input("'Simple' or 'Compound' interest: ").lower()           # cast this input to the lower() function to change user input to lower characters 
elif calculation == "bond":                                                 # so that its easier to work with
    present_value = float(input("Current value of house(R): "))
    interest_rate = float(input("Interest rate(%): "))
    repay_time = float(input("Number of months you choose to repay the bond: "))
else:
    print("Sorry wrong calculation.")

#  bond variables
# I changed the input variables to simpler variables to use in formula
#   x = (i.p)/(1-(1+i)^(-n))
P = float(present_value)
i = float((interest_rate/100)/12)            # divide interest rate by 100 to get annual interest rate then divide by 12 to get monthly interest rate
n = float(repay_time)

# performing the calculation depending on the users input
# it performs two different investment calculations depending on compound or simple interest
# if user selected bond then it jumps straight to the bond formula
if calculation == "investment":
    if interest == "simple":
        final_amount = round((paid_amount * (1 + (interest_rate/100) * years)), 2)
        print(f'Your final amount will be R{final_amount}')
    elif interest == "compound":
        final_amount = round((paid_amount * math.pow((1 + (interest_rate/100)), years)), 2)
        print(f'Your final amount will be R{final_amount}')
    else:
        print("Wrong interests rate")
elif calculation == "bond":
    x = round((i*P)/(1-(1+i)**(-n)), 2)
    print(f'You will have to repay R{x} each month for your bond')
else:
    print("Please try again")       # this displays if user did not select the correct calculation to perform

