import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19, GPIO.OUT)

GPIO.output(19, GPIO.LOW)
os.system("pkill idle")
