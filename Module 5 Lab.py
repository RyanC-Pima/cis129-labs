# Module 5 Lab
#Ryan Calles
#CIS 129
#Asks for number of bottles returned to the store each week and calculates the refund amount paid out

# declare variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

#condition that enables loop to repeat
while keepGoing == 'y':

    #increments counter until 7 days is reached, keeps running total of bottles, and calculates payout amount based on total
    for counter in range(7):
        counter += 1
        todayBottles = int(input(f'Enter the number of bottles for day #{counter}: '))
        totalBottles += todayBottles
        totalPayout = totalBottles * .1

    #displays number of bottles and total paid out    
    print('\nThe total number of bottles collected is', totalBottles)
    print(f'The total paid out is ${totalPayout:,.1f}')
    #resets variables to be used in next loop
    counter = 1
    totalBottles = 0
    #asks user if they want to enter data for a new week
    print('\nDo you want to enter another week\'s worth of data?')
    keepGoing = input('(Enter y or n): ')
    print('')