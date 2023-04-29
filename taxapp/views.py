from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
taxrate = 15
def view1 (request):
    return render (request,"taxapp/lab44.html") 

def view2 (request, number ):
    number = number +(taxrate/100*number)
    return HttpResponse (number)

def view3(request):
    return render (request,"taxapp/TAXRATE.html",{"taxrate":taxrate})



