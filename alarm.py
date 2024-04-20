#import modules to be used
import time
import datetime

while True:
# Get user input for alarm
    alarm = input("Enter time for alarm. (Eg 06:30): ")
    hour = alarm [0:2]
    minute = alarm [3:5]
    
    hour_sec = int(hour) * 3600
    minute_sec = int(minute) * 60
    #Calculating the total time in seconds
    total = int(hour_sec) + int(minute_sec)

    #Check if time entered is valid
    if (int(hour) >= 0 and int(hour) <= 23 and int(minute) >= 0 and int(minute) <= 59):
        print("The hour is: ", hour)
        print("The minute is: ",minute)
        
        print ("Time in seconds is ", hour_sec, ":", minute_sec)
        print("Total time in seconds = ", int(total))
        
        break
    else:
        print("Invalid time")
        
        hour_sec = int(hour) * 3600
        minute_sec = int(minute) * 60

#To get present time
now = datetime.datetime.now()

now_sec = now.hour *3600 + now.minute *60

print("Current time is: ",now)
print("Current time in seconds is: ",now_sec)


#Check time left to alarm and ring
if (int(now_sec)<int( total)):
    wait=total-now_sec 
    print ("time left: ", wait)
    time.sleep(wait)
    print("wake up")
    
else:
    print("It's past time!")

#print("Current time is: ",now)
