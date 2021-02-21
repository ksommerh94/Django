from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
# Create your views here.
def index(request):
    #retrieve items from database
    items=Item.objects.all()
    print(items)

    #adding item to database
    if request.method=="POST":
        name = request.POST["name"]
        detail= request.POST["detail"]

        newItem=Item(name= name,detail=detail)
        newItem.save()
        return redirect ("/core")

    context={
        "itemList":items
    }

    return render(request,"body.html",context)
