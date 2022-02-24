from http.client import HTTPResponse
from re import search
from django.http import HttpResponse
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
            productImage = i.image
            productPrice = i.price
            productDetail = i.detail
    return render(request, 
            "productInfo/productInfo.html",
            {"x": databaseInfo,
            "productName": productName,
            "productImage": productImage,
            "productPrice": productPrice,
            "productDetail": productDetail,
            }) 

def searchItem(request):
    itemSearched = request.GET["itemName"]
    iSplitter = itemSearched.split()
    iSplitterLen = len(iSplitter)
    foundProducts = []

    databaseInfo = JobsConfig.objects.all()

    for item in databaseInfo: # filter searched
        if iSplitterLen == 1: # if searched only one word
            if item.name == itemSearched or itemSearched in item.name or itemSearched.lower() in item.name or itemSearched.upper() in item.name or itemSearched.capitalize() in item.name:
                productName = item.name
                productImage = item.image
                productPrice = item.price
                productDetail = item.detail
                foundProducts.append(item)

        elif iSplitterLen > 1: # if searched more than one word
            for word in iSplitter:
                if word in item.name or word.lower() in item.name or word.upper() in item.name or word.capitalize() in item.name:
                    productName = item.name
                    productImage = item.image
                    productPrice = item.price
                    productDetail = item.detail
                    foundProducts.append(item)


    return render(
            request,
            "search.html",
            {"x": databaseInfo,
            "productName": productName,
            "productImage": productImage,
            "productPrice": productPrice,
            "productDetail": productDetail,
            "foundProducts": foundProducts,
            })

def about(request):
    return render(request, 'about.html')