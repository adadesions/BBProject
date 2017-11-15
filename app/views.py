from django.shortcuts import render, HttpResponse

def index( req ):
    return render( req, 'app/index.html')

def detail( req ):
    return HttpResponse("Hey! Ada") 
