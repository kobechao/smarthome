import bluetooth
import time
import RPi.GPIO as GPIO
import json

from threading import Thread
import datetime
from random import randint
import Queue

import subprocess
import time, datetime
import json
import MFRC522



import sys

devices = dict()
output = dict()

SPACE = 'space'
RPIN = 'rPin'
GPIN = 'gPin'
PEOPLE = 'people'
DEVICE = 'device'

UNKNOWN = '[Unknown]'


# flag
def initOutput() :
    output[RPIN] = ''
    output[GPIN] = ''
    output[SPACE] = ''
    output[PEOPLE] = ''
    devices[DEVICE] = ''

def outputJSON() :
    print output
    with open ( 'device_space.json', 'w+' ) as f :
        f.write( json.dumps( output ) )
        f.close()

def generateAccess() :
    print 'generate'
    data = dict()
    with open( 'loginData.json', 'w+' ) as f :
        data['user'] = 'pi'
        data['password'] = '00000000'
        f.write( json.dumps( data ) )
        f.close()


def getCurrentTime () :
    now = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return str( now ), '-' * len( now )


def checkConnectingWifi( targetWifi ):

    connected = False ; timeout = 0
    while not connected :

        try:
            ssid = subprocess.check_output( [ 'iwgetid -r' ], shell=True  )
            print ssid.strip( '\n' )

            if targetWifi == ssid.strip( '\n' ) :
                # sendFile()
                print True
                connected = True
                return True
            else :
                connected = False
                print "Untargeted wifi!"


        except Exception as e:
            print e, "reconnected"
            connected = False

        time.sleep( 1 ) ; timeout += 1

        if timeout >= 30 :
            return False
            sys.exit(1)

    return False


def finish() :
    print "Finish!"
    sys.exit( 0 )


# functions
def detecting( ) :

    TAG = 'Blutooth Serching...'

    target_name = "Kobechao"
    target_address = None

    while True :

        now, _tag = getCurrentTime()
        print "%s\n%s\n%s" % ( TAG, now, _tag )

        rlt = []
        nearby_devices = bluetooth.discover_devices()

        for bdaddr in nearby_devices:
            name = bluetooth.lookup_name( bdaddr )
            if target_name == bluetooth.lookup_name( bdaddr ):
                target_address = bdaddr
            tmp = []
            tmp.append( bdaddr ) ; tmp.append( name )
            rlt.append( bdaddr )


        with open( 'flowtable_device.json', 'r' ) as f :
            flow = json.loads( f.read() )
            try:
                output[SPACE] = flow[ rlt[0] ]
                pass
            except Exception as e:
                print 'Unknown devices!!\n'

            f.close()

        print rlt, "rlt"
        outputJSON()


def gpioTest( ) :

    TAG = 'GPIO TEST'
    print TAG
    rPin = 3; gPin = 5
    GPIO.setup( rPin, GPIO.OUT )
    GPIO.setup( gPin, GPIO.OUT )

    GPIO.output( rPin, 0 ); GPIO.output( gPin, 0 )

    if output[PEOPLE] == 'Kobe' :
        GPIO.output( rPin, 1 )
        output[RPIN] = 'ON'
    else :
        GPIO.output( rPin, 0 )
        output[RPIN] = 'OFF'

    if output[PEOPLE] == 'Cindy':
        GPIO.output( gPin, 1 )
        output[GPIN] = 'ON'
    else :
        GPIO.output( gPin, 0 )
        output[GPIN] = 'OFF'

    outputJSON()

    # space = ''

    # while True :

    #     now, _tag = getCurrentTime()
    #     print '%s\n%s\n%s' % ( TAG, now, _tag )

    #     rFlag = randint( 0, 1 )
    #     GPIO.output( rPin, rFlag )
    #     gFlag = randint( 0, 1 )
    #     GPIO.output( gPin, gFlag )


    #     if rFlag :
    #         output[RPIN] = 'ON'
    #     else :
    #         output[RPIN] = 'OFF'

    #     if gFlag :
    #         output[GPIN] = 'ON'
    #     else :
    #         output[GPIN] = 'OFF'

    #     outputJSON()

    #     time.sleep(2)



def RFID() :
    MIFAREReader = MFRC522.MFRC522()

    # Welcome message
    print "Welcome to the MFRC522 data read example"
    print "Press Ctrl-C to stop."

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while True:

        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            UID = str( uid[0] ) + "," + str( uid[1] ) + "," + str( uid[2] ) + "," + str( uid[3] )
            print "Card read UID: " + UID

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag( uid )

            # Authenticate
            status = MIFAREReader.MFRC522_Auth( MIFAREReader.PICC_AUTHENT1A, 8, key, uid )

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                MIFAREReader.MFRC522_Read( 8 )
                MIFAREReader.MFRC522_StopCrypto1()

                with open( 'flowtable_person.json', 'r' ) as f :
                    flow = json.loads( f.read() )
                    try:
                        output[PEOPLE] = flow[ UID ]
                    except Exception as e:
                        print 'Unknown people!!'
                        output[PEOPLE] = UNKNOWN

            else:
                print "Authentication error"


            # outputJSON()
            gpioTest()



def main () :

    targetSSID = 'Kobechao'
    jobs = []
    if checkConnectingWifi( targetSSID ) :

        generateAccess()
        initOutput()

        bluetoothThread = Thread( target=detecting, args=() )
        # GPIOThread = Thread( target=gpioTest, args=() )
        RFIDThread = Thread( target=RFID, args=() )
        try:
            bluetoothThread.start()
            RFIDThread.start()
            # GPIOThread.start()

        except:
            bluetoothThread.join()
            RFIDThread.join()
            # GPIOThread.join()
            sys.exit( 1 )

        # RFID()

        pass



if __name__ == '__main__' :

    try :
        main()

    except Exception as e :
        print type(e), e
        print sys.exc_info()

    finally:
        finish()



