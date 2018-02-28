#Benet Morando BIS 415
#Sugar Shake Beta via Python 3.6.1
#Week 4 for capstone: glucose recorder
#05/07/17
################################################################

class recorder():
    glucose_level = int(input("What is your blood sugar level?"))
    timeoftest = input("What time was that test taken?")

    print("Okay so here is what we have just recorded")
    print("Here is what your glucose level is right now")
    print(glucose_level)
    print("Here is the time that you checked that BG level")
    print(timeoftest)

#this is to alert the user of the status of the blood sugar they entered. 
'''     
if glucose_level < 70:
    print("Your blood sugar is dropping low so please eat or drink something to get it above 70")

elif glucose_level > 70 and glucose_level < 180:
    print("Your blood sugar level is normal, keep up the good work")
else:
    print("Your blood glucose level is dangerously high, please seek medical attention to get it to normal levels or take medication.")'''
            




   
    
