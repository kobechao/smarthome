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
        import json
        print( devices['device'] )
        pathDevice = json.loads( devices['device'] )
        print( pathDevice )
        index = list( pathDevice.keys() )[0]
        print( index )
        path = 'Data/%s' % index
        print( path )
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
            print( DEVICE_NAME)

        try :
            with open( os.path.join( os.getcwd(), path ) + "/login.json" , "w+" ) as rlt :
                import json
                # print( "open file" )
                rlt.write( json.dumps( loginDatas ) )
                rlt.close()

            if os.path.isfile( 'all_login.json' ) :
                with open( 'all_login.json', 'r' ) as f :
                    all_login = json.loads( f.read() )
                    print( all_login )
                    all_login.update( { loginDatas['device_id']: loginDatas } )
                    with open( 'all_login.json', 'w+' ) as allFile :
                        allFile.write( json.dumps( all_login ) )
                        allFile.close()
            else :
                with open( 'all_login.json', 'w+' ) as allFile :
                    all_login = {}
                    all_login[ loginDatas['device_id'] ] = loginDatas
                    allFile.write( json.dumps( all_login ) )
                    allFile.close()

        except Exception as e :
            print( type(e), e )




    return render( req, 'login.html' )