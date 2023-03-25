from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

productss=[
        {'Name':'Phone Adapter',
         'Price':1000,
         'Quantity':50,
         },{'Name':'Television',
         'Price':40000,
         'Quantity':20,
         },{'Name':'Refrigerator',
         'Price':25000,
         'Quantity':25,
         },{'Name':'Microwave',
         'Price':10000,
         'Quantity':50,
         },{'Name':'Speaker',
         'Price':8000,
         'Quantity':35,
         }
    ]
def prdct(request):
    context={'products':productss}
    return render(request, 'product/home.html',context)

