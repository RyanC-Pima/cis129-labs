# Module 4 Lab
#Ryan Calles
#CIS 129
#This program asks the user for Monthly Sales and Percent of Sales Increase in order to calculate store and employee bonus amounts.

# declare local variables
monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0

# This code gets the monthly sales
monthlySales = float(input('Enter the monthly sales $'))

# This code determines the storeAmount bonus
if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
	storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
else:
    storeAmount = 0
	
# This code gets the percent of increase in sales
salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')  
