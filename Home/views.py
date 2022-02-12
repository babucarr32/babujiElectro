from django.shortcuts import render
from .models import homeModel

def homePage(request):
    databaseInfo = homeModel.objects
    i = 10
    return render(request, 
                "index.html",
                {"jobs": databaseInfo,
                "x": i},
                
                )