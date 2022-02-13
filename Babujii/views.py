from django.shortcuts import render

def homePage(request):
    databaseInfo = "omeModel.objects"
    i = 10
    return render(request, 
                "index.html",
                {"jobs": databaseInfo,
                "x": i},
                
                )