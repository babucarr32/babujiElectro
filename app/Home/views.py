from django.shortcuts import render
from .models import JobsConfig


def homePage(request):
    databaseInfo = JobsConfig.objects.all()
    i = 10
    return render(request, 
                "index.html",
                {"jobs": databaseInfo,
                "x": i},
                
                )

def productInfo(request, pk):
    databaseInfo = JobsConfig.objects.all()

    for i in databaseInfo:
        if i.id == pk:
            productName = i.name
            productImage = i.image.url
            productPrice = i.price
            productDetail = i.detail
    return render(request, 
            "jobs/productInfo.html",
            {"x": databaseInfo,
            "productName": productName,
            "productImage": productImage,
            "productPrice": productPrice,
            "productDetail": productDetail,
            }) 
