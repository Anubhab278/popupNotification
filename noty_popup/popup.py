from plyer import notification
from time import sleep
from datetime import*
import timeAct


    
def notify_all(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\\work space\\noty_popup\\clock.ico",
        timeout = True
)



if __name__ == '__main__':

    hour = int(input("enter the hour when you want to get notified"))
    minute = int(input("enter the munits when you want to get notified"))
    while True:
        
        k = timeAct.currentTime()
        if(k[0] == hour and k[1] == minute):
            
            notify_all("ALART","Hii there!!! I am your reminder machine")        
            print("successful")
            sleep(30)
           
        
