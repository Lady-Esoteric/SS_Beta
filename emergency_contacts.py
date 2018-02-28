#Benet Morando BIS 415
#Sugar Shake Beta via Python 3.6.1
#Week 4 for capstone : Emergency contacts
#4/17/17
################################################################
#this is where they will be able to update their data for who they want
#to be on call during the alert being activated
print("Okay so you want to input some emergency contacts?")
print("Lets get started!!")
print("****************************************************")

class emergency_contact:
    contact_id = input("What Id do you want to give this contact choose from 1-10? ")
    contacts_full_name = input("So what is the name of this emergency contact? ")
    contacts_phonenumber = input("What phone number can we reach this person by? ")

    print("Okay so far we have", contacts_full_name, "\n who you have as contact number", contact_id, "\n who can be contacted at this number", contacts_phonenumber)
    print("Is this correct?")

    user_input = input("Yes or no?")

    #if -else statement to placed here to make sure that all is good to go and that the information is correct.
    
    
    
