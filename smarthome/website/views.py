from django.shortcuts import render, redirect
import os

DEVICE_NAME = ''

def index( request ):
    if request.GET :
        print( request.GET )
    return render( request, 'index.html' )

def generic( req ) :

    if req.GET :
        devices = req.GET
        print( DEVICE_NAME )
        path = 'Data/%s' % DEVICE_NAME
        if not os.path.isdir ( path ) :
            os.makedirs ( path )

        with open( os.path.join( os.getcwd(), path ) + '/devices.json' , "w+" ) as rlt :
            import json
            print( "open file" )
            rlt.write( json.dumps( devices['device'] ) )
            rlt.close()

    return render( req, 'generic.html' )


def light( req ) :

    if req.GET :
        lightStatus = req.GET
        print( lightStatus['device'] )

    return render( req, 'light.html' )


def login( req ) :

    if req.GET :
        loginDatas = req.GET
        print( loginDatas )
        path = 'Data/%s' % loginDatas['device_id']

        if not os.path.isdir ( path ) :
            os.makedirs ( path )
            DEVICE_NAME = loginDatas['device_id']

        with open( os.path.join( os.getcwd(), path ) + "/login.json" , "w+" ) as rlt :
            import json
            print( "open file" )
            rlt.write( json.dumps( loginDatas ) )
            rlt.close()

    return render( req, 'login.html' )