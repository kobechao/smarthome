import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM )

def lightOnOff( ledpin, switch ) :
    GPIO.setup( ledpin, GPIO.OUT )
    if switch == 'ON'.upper() :
        GPIO.output( ledpin, True )
    elif switch == 'OFF'.upper()
        GPIO.output( ledpin, False )
    else :
        print( "None Avaliable" )




if __name__ == '__main__':
    lightOnOff( 17, 'ON' )