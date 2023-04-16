from django.shortcuts import render

# Create your views here.
def getmethod(request):
    return render(request,'getmethod.html')