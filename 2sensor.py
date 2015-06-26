import RPi.GPIO as GPIO
import time
import pygame
import random

pygame.init()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG=20
ECHO=21

TRIG2=23
ECHO2=24

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.output(TRIG2, GPIO.LOW)
time.sleep(0.3)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
time.sleep(0.3)

def measure():
        GPIO.output(TRIG2, True)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	GPIO.output(TRIG2, False)
	first_start=0
	second_start=0

	first_end =0
	second_end =0
	while GPIO.input(ECHO)==0 and GPIO.input(ECHO2)==0:
                first_start=time.time()
                second_start=time.time()
        while GPIO.input(ECHO)== 1 and GPIO.input(ECHO2) ==1:
                first_end = time.time()
                second_end=time.time()
        # Front sensor
                
        #Back Sensor

        if first_end ==0 and second_end==0:
                return 0
	first_duration=first_end-first_start
	second_duration=second_end-second_start
    
	first_distance=first_duration*17150
	second_distance=second_duration*17150

	first_distance=round(first_distance,2)
	second_distance=round(second_distance,2)

	if first_distance < 10 and second_distance < 10:
		if first_end < second_end :
			print "Book Arrangement is Sensed"
			picknum=random.randint(1,4)

			if picknum==1 :
				fn="1.wav"
			elif picknum==2 :
				fn="2.wav"
			elif picknum==3 :
				fn = "3.wav"
			elif picknum==4:
				fn="4.wav"

			pygame.mixer.music.load(fn)
			pygame.mixer.music.play()
			time.sleep(4.7)
	return 0

while True:
	measure()





