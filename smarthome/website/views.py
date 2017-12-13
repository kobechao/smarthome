from django.shortcuts import render, redirect
# from light import lightOnOff

def index( request ):
    if request.GET :
        print( request.GET )
    return render( request, 'index.html' )

def generic( req ) :

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

    if req.GET :
        loginDatas = req.GET
        print( loginDatas )
        with open( "login.json", "w+" ) as rlt :
            import json
            print( "open file" )
            # rlt.write( json.dumps( loginDatas.pop(, None ) ) )
            rlt.write( json.dumps( loginDatas ) )
            rlt.close()

    return render( req, 'login.html' )