# Future Value Program
#Jeremy Bargy
#Jan. 10, 2020 
# 
# Converting a Math Formula to a Programming Statement

# Determining the amount value to deposit in a savings account
# to reach desired future value in a set amount of time.

# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate.
rate = float(input('Enter the annual interest rate: '))

#Get the number of years that the money will appreciate.
years = int(input('Enter the number of years the money will grow: '))

#Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

#Display the amount needed to desposit.
print('You will need to deposit this aount:', format(present_value, '.2f'))
