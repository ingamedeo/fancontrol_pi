import RPi.GPIO as GPIO
import os
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(22, GPIO.OUT)
while 1==1:
	f=os.popen("/home/ingamedeo/temp.sh")
	for i in f.readlines():
		row=(i[0:4])
	row = float(row)
	if row > 50:
		print "HIGH - ", row
		GPIO.output(22, True)
		time.sleep(60*15)
	else:
		print "LOW - ", row
		GPIO.output(22, False)
		time.sleep(2)
