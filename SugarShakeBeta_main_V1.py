#Benet Morando BIS 415
#Sugar Shake Beta via Python 3.6.1
#Week 4 for capstone
#4/17/17
################################################################
'''import sys
import userinformation
import glucose_recorder
import emergency_contacts
import glucose_records'''

#this will be pulling in the other modules of this beta application

#The menu below will show for the users so that they may proceed with usage
print("Sugar Shake Beta: Helping you keep your sugar in check:")
print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|--|-|-|-|-|-|-|-|-|-|-|-|-|--|-|-|-|-|-|-|-")
print("Please review the menu below and choose your option: ")
print(" 1 = User information ")
print(" 2 = Enter/Record glucose level ")
print(" 3 = Emergency Contacts ")
print(" 4 = Glucose records view ")

user_input = input("What is the option you have chosen: ")

# /if-else statement will be placed here to determine where
#the user will be led to after they make their selection
# when the user makes their choice that input will have the information imported
if user_input == '1':
    import userinformation

elif user_input == '2':
    import gluscose_recorder

elif user_input == '3':
    import emergeny_contacts

elif user_input == '4':
    import glucose_records

else:
    print("Thank you for using Sugar Shake Beta.")
   
          


    

