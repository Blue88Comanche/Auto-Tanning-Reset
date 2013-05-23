#Jeffrey Enfinger
#auto tanning reset
#Beta version
###
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)
while True:
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    now_date = str(month) + '/' + str(day) + '/' + str(year)
    now_time = str(hour) + ':' + str(minute) + ':' + str(second)
    print now_time
    print now_date
    print 'running'
    if hour is 00:
        if minute is 00:
            if second is 00:
                print "reset"
                GPIO.output(12, GPIO.LOW)
                text_file = open("tanning reset log.txt", "a")
                text_file.write("Reset tanning" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
                text_file.close()
                import time
                time.sleep(1)
                GPIO.output(12, GPIO.HIGH)
    import time
    time.sleep(1)
