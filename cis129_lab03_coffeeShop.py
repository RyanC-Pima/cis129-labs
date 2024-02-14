# cis129_lab03_coffeeShop.py
"""This program generates a receipt for Ryan's Coffee and Muffin Shop."""


# Ask user for number of each item bought.  Convert all input strings to integers.
print('***************************************')
print('Ryan\'s Coffee and Muffin Shop')
numberOfCoffees = int(input('Number of coffees bought?\n'))
numberOfMuffins = int(input('Number of muffins bought?\n'))
numberOfTeas = int(input('Number of teas bought?\n'))
numberOfCroissants = int(input('Number of croissants bought?\n'))
print('***************************************')

# Calculate cost of each item ordered
coffeeCost = numberOfCoffees * 5
muffinCost = numberOfMuffins * 4
teaCost = numberOfTeas * 4
croissantCost = numberOfCroissants * 3

# Calculate subtotal of all items, calculate 6% tax based on subtotal, then calculate total cost by adding subtotal + tax
subtotal = coffeeCost + muffinCost + teaCost +croissantCost
tax = subtotal * .06
totalCost = subtotal + tax

# Add pluralization for menu item strings with values other than 1.
coffeePlural = str
if numberOfCoffees == 1:
    coffeePlural = ''
else:
    coffeePlural = 's'

muffinPlural = str
if numberOfMuffins == 1:
    muffinPlural = ''
else:
    muffinPlural = 's' 

teaPlural = str
if numberOfTeas == 1:
    teaPlural = ''
else:
    teaPlural = 's'

croissantPlural = str
if numberOfCroissants == 1:
    croissantPlural = ''
else:
    croissantPlural = 's'       

# Print counts and cost of each item, print tax, and print total cost.  Format 2 digit decimal for currency values.
print('\n\n***************************************')
print('Ryan\'s Coffee and Muffin Shop Receipt')
print(numberOfCoffees, ('Coffee' + coffeePlural), 'at $5 each: $', (format(coffeeCost, ',.2f')))
print(numberOfMuffins, ('Muffin' + muffinPlural), 'at $4 each: $', (format(muffinCost, ',.2f')))
print(numberOfTeas, ('Tea' + teaPlural), 'at $4 each: $', (format(teaCost, ',.2f')))
print(numberOfCroissants, ('Croissant' + croissantPlural), 'at $3 each: $', (format(croissantCost, ',.2f')))
print('6% tax: $', (format(tax, ',.2f')))
print('---------')
print('Total: $', (format(totalCost, ',.2f')))
print('***************************************')
print('Thank you for stopping by today!')
print('We hope to see you again soon!')
