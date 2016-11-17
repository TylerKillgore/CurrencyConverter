#CurrencyConverter.py 
#Scripted by Tyler Killgore
#Description: Converts USD to Euro

#1 USD = .93 Euro
#1 Euro = 1.07 USD

def currencyConvert():
    #Find out what user wants to convert 1).USD -> Euro 2). Euro -> USD
    # Store answer into a variable
        userChoice = raw_input ("What do you want to convert? \n1) USD > Euro \n2) Euro > USD")
        print userChoice
    #Check and see what user typed
    
    #If user typed 1 
        if userChoice == 1: 
    #Prompt the user the amount of USD they want to convert
            print "choice = 1"
    #Store what the user typed into a variable
    #Euro = USD amount * .93
    #Output amount to user
    
    #If user typed 2
        elif userChoice == 2:
    #Prompt the user the amount of USD they want to convert
            print "choice = 2"
    #Store what the user typed into a variable
    #USD = Euro amount * 1.07
    #Output amount to user
    
    #if user typed anything else 
        else:
    #do something
            print "error"
    
currencyConvert()