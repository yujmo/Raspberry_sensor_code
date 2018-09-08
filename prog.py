import RPi.GPIO
import time
SENSOR = 4
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(SENSOR, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(LED, RPi.GPIO.OUT)
try:
	while True:
    	print(RPi.GPIO.input(SENSOR))
except KeyboardInterrupt:
	pass
RPi.GPIO.cleanup()