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
    elif status =='ON' :
        GPIO.output(ledPin, True)

    time.sleep(1)

if __name__ == '__main__' :
    import sys
    print 'start'
    if len( sys.argv ) != 2 :
        print 'Give an argument of switch'
        sys.exit(0)

    switch( sys.argv[1] )
