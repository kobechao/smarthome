from django.shortcuts import render
# from light import lightOnOff

def index( request ):
    return render( request, 'index.html' )

def generic( req ) :
    print( req )
    print( "XXX" )
    if req.GET :
        devices = req.GET
        print( devices['device'] )
        with open( "devices.json", "w+" ) as rlt :
            import json
            print( "open file" )
            rlt.write( json.dumps( devices['device'] ) )
            rlt.close()


    return render( req, 'generic.html' )


def light( req ) :
    if req.GET :
        lightStatus = req.GET
        print( lightStatus['device'] )
        # lightOnOff( 17, posts['switch'] )

    return render( req, 'light.html' )


def login( req ) :
    return render( req, 'login.html' )