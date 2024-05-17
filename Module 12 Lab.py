# Module 12 Lab
# Ryan Calles
# CIS 129
# Ask user for pet info; store data and display to user

# main module
def main():
    
    # Declare input variables  	
    animalName = str
    animalType = str
    animalAge = int

    # class variable to hold a pet
    animal = Pet()
 
    # create a Pet object
    animal = Pet(animalName, animalType, animalAge)
 
    # Get values for a pet
    print('Enter your pet\'s name:')
    animalName = input()
    animal.setName(animalName)
	
    print('Enter your pet\'s type:')
    animalType = input()
    animal.setType(animalType)
	
    print('Enter your pet\'s age:')
    animalAge = input()
    animal.setAge(animalAge)
 
    #Show values for this pet
    print('Your pet name:', animal.getName())
    print('Your pet type:', animal.getType())
    print('Your pet age:', animal.getAge())    
 
 
class Pet:
  	#constructor
    def __init__(self, n='', t='', a=0):
        self.name = n
        self.type = t
        self.age = a 

    #mutators
    def setName(self, n):
        self.name = n
    
    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a 
    
    #accessors
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getAge(self):
        return self.age    

main()