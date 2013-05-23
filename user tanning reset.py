import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.output(12, GPIO.HIGH)
while True:
    input = GPIO.input(11)
    if input:
        from datetime import datetime
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        import time
        time.sleep(1)
        now_date = str(month) + '/' + str(day) + '/' + str(year)
        now_time = str(hour) + ':' + str(minute) + ':' + str(second)
        text_file = open("tanning reset log.txt", "a")
        text_file.write("Manual Reset tanning" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
        text_file.close()
        GPIO.output(12, GPIO.LOW)
        time.sleep(5)
        GPIO.output(12, GPIO.HIGH)
