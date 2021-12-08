from datetime import*

def currentTime():
    time = str(datetime.time(datetime.now()))
    hours = int(time[0:2])
    munits = int(time[3:5])
    return hours,munits

    
    
