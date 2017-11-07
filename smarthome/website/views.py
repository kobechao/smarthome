from django.shortcuts import render
# from light import lightOnOff

def index( request ):
    return render( request, 'index.html' )

def generic( req ) :
    return render( req, 'generic.html' )

def light( req ) :
    # if req.POST :
    #     posts = req.POST
    #     print( posts['switch'] )
    #     lightOnOff( 17, posts['switch'] )

    return render( req, 'light.html' )

def fjs( req ) :
    return render( req, 'fjs.html' )

def login( req ) :
    return render( req, 'login.html' )