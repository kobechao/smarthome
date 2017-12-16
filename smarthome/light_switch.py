#!/usr/bin/python

def switch( status ) :
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BOARD)
    ledPin = 12
    GPIO.setup(ledPin, GPIO.OUT)

    print "Starting... "
    if status == 'OFF' :
        GPIO.output(ledPin, False)
    elif status ==' ON' :
        GPIO.output(ledPin, True)

    time.sleep(1)
