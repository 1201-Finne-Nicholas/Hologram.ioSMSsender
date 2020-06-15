#Importing OS to use command lines

import os
import sys

print(os.environ)
print (sys.version)
print (sys.version_info)

#Starter menu for the user
while True:

    menuInput = input(" 1. Add new phone number \n\n 2. See current phone numbers on the list \n\n 3. Send a message to the list of phone numbers \n\n 4. Clear all phone numbers on list \n\n 5. Run cellular_test.py \n\n 6. Connect to hologram network \n\n 7. Disconnect from hologram network \n\n 8. Exit \n\n")

    #   Menu's Sections
    if (menuInput == "1"): 
        # Adds new numbers to Phone Numbers List text file
        PhoneNumbers = open("PhoneNumbersList.txt", "a+")
        newPN = input("Type in phone number:\n")
        PhoneNumbers.write(newPN)
        PhoneNumbers.write("\n")
        PhoneNumbers.close()
        
    elif (menuInput == "2"): 
        # Reads out the phone numbers on the text file to user
        PhoneNumbers = open("PhoneNumbersList.txt", "r")
        numbers = PhoneNumbers.read()
        print(numbers)
        PhoneNumbers.close()
    elif (menuInput == "3"):
        # Asks user for a message to send to the phone numbers
        textMessage = input("\nWhat would you like to send out to the phone numbers?\n")
        PhoneNumbers = open("PhoneNumbersList.txt", "r")
        pnumbers = PhoneNumbers.readlines()
        i = 0 # Used as a counter to send each line of text in the Phone Numbers text file or in this case to send each phone number
        for x in pnumbers:
            if(pnumbers != ""):
                print('"+{0}", "{1}"' .format(pnumbers[i], textMessage))
                #cloud.sendMessage('"+{0}", "{1}"' .format(pnumbers[i], textMessage))
                i = i + 1
        PhoneNumbers.close()
    elif (menuInput == "4"): 
        # Clears all numbers on the text file
        clrFileinp = input("\n Are you sure? \n\n 1. Yes \n\n 2. No \n\n")
        if (clrFileinp == "1"): #Double checking if the user wants to do so
            PhoneNumbers = open("PhoneNumbersList.txt", "w+")
            PhoneNumbers.write("")
            print("\n Cleared all phone numbers on the list \n")
            PhoneNumbers.close()
    elif (menuInput == "5"):
        cellular_test()
    elif (menuInput == "6"): 
        os.system("sudo hologram network connect")
    elif (menuInput == "7"): 
        os.system("sudo hologram network disconnect")
    elif (menuInput == "8"): 
        # Exits app
        print("Exiting")
        break
