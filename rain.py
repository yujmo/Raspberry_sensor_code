import RPi.GPIO as GPIO
 
import time
 
GPIO.setmod(GPIO.BCM)
 
GPIO.setup(17,GPIO.IN)

while True:

  if GPIO.input(18):
     print("no rain")
  else:
     print("rain")
  time.sleep(1)
