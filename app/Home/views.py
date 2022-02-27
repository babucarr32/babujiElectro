from http.client import HTTPResponse
from re import search
from requests import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import JobsConfig


try:
    def homePage(request):
        databaseInfo = JobsConfig.objects.all()
        outOfStock=[]
        inStock=[]
        for item in databaseInfo:
            if item.price == 0:
                outOfStock.append(item)
            else:
                inStock.append(item)

        i = 10
        
        return render(request, 
                    "index.html",
                    {"inStock": inStock,
                    "outOfStock": outOfStock,
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
                if productPrice == 0:
                            print("Out of stock----------------------------------------------------------------------------------------")

        return render(request, 
                "productInfo/productInfo.html",
                {"x": databaseInfo,
                "productName": productName,
                "productImage": productImage,
                "productPrice": productPrice,
                "productDetail": productDetail,
                }) 

    def searchItem(request):
        productNotFound = False
        itemSearched = request.GET["itemName"]
        iSplitter = itemSearched.split()
        iSplitterLen = len(iSplitter)
        outOfStock=[]
        inStock=[]
        foundProducts = []

        databaseInfo = JobsConfig.objects.all()

        if iSplitterLen == 1: # if searched only one word
            for item in databaseInfo: # filter searched
            
                if item.name == itemSearched or itemSearched in item.name or itemSearched.lower() in item.name or itemSearched.upper() in item.name or itemSearched.capitalize() in item.name:
                    if item.price == 0:
                        outOfStock.append(item)
                    else:
                        inStock.append(item)
                    foundProducts.append(item)
                    productNotFound = False
                else:
                    productNotFound =True

        elif iSplitterLen > 1: # if searched more than one word
            for word in iSplitter:
                for item in databaseInfo:
                    if word in item.name or word.lower() in item.name or word.upper() in item.name or word.capitalize() in item.name:
                        if item.price == 0:
                            outOfStock.append(item)
                        else:
                            inStock.append(item)
                        productNotFound = False
                    else:
                        productNotFound = True
        if productNotFound == True:
            with open(r"Babujii\logs\unfoundSearches.txt", "a") as f:
                ip = get('https://api.ipify.org').text
                print(ip)
                f.write(f"|  {itemSearched.ljust(54)}| {ip.ljust(30)}  |\n")
            print("Sorry! no product found. ---------------------------------------------------------------")
            return render(request, "productNotFound.html")

        return render(
                request,
                "search.html",
                {"x": databaseInfo,
                "inStock": inStock,
                "outOfStock": outOfStock,
                })

    def about(request):
        return render(request, 'about.html')
except Exception as e:
    homePage()
