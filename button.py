import RPi.GPIO as GPIO
import time
import socket
import random
import requests

url= "http://:8080" #The IPaddress your conntecting to

hostname = socket.gethostname()


greaterThan = float(input("Your number will be greater than: "))
lessThan = float(input("Your number will be less than: "))
digits = int(input("Your number will have that many decimal digits: "))

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(18)
	if input_state == False:

		rounded_number = round(random.uniform(greaterThan, lessThan), digits)
                #Change the Pi number to the number on your box
		payload = {'RaspberryPi Number':'26',
               'Title': 'Temperature of RaspberryPi',
               'Temperature':rounded_number,
               'Time':''}

    		print(payload)
   		post_data = requests.post(url, json=payload)
		time.sleep(0.2)
