# cis129_lab03_coffeeShop.py
"""This program generates a receipt for Ryan's Coffee and Muffin Shop."""


# Ask user for number of coffees bought, and number of muffins bought.  Convert both inputs to integers.
print('***************************************')
print('Ryan\'s Coffee and Muffin Shop')
numberOfCoffees = int(input('Number of coffees bought?\n'))
numberOfMuffins = int(input('Number of muffins bought?\n'))
print('***************************************')

# Calculate cost of each item ordered
coffeeCost = numberOfCoffees * 5.00
muffinCost = numberOfMuffins * 4.00

# Calculate subtotal of all items, calculate 6% tax based on subtotal, then calculate total cost by adding subtotal + tax
subtotal = coffeeCost + muffinCost
tax = subtotal * .06
totalCost = subtotal + tax

# Add pluralization for coffee and muffin values other than 1.
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

# Print counts and cost of each item, print tax, and print total cost.  Format 2 digit decimal for currency values.
print('\n\n***************************************')
print('Ryan\'s Coffee and Muffin Shop Receipt')
print(numberOfCoffees, ('Coffee' + coffeePlural), 'at $5 each: $', (format(coffeeCost, ',.2f')))
print(numberOfMuffins, ('Muffin' + muffinPlural), 'at $4 each: $', (format(muffinCost, ',.2f')))
print('6% tax: $', (format(tax, ',.2f')))
print('---------')
print('Total: $', (format(totalCost, ',.2f')))
print('***************************************')
