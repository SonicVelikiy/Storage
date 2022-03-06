from django.shortcuts import render, redirect
from .models import Inproduct,Outproduct,BalanceStorage
from .forms import addproduct
from django.views import View

def HistoryStorage(request):
    search = request.GET.get("search")
    if search is None:
        inproduct = Inproduct.objects.all()
    else:
        inproduct = Inproduct.objects.filter(name__contains=search)
    return render(request,"itm/home.html",{"inproduct":inproduct})

class CreateProduct(View):
    #mahsulot qo'shish tarixini ishlab chiqish kerak
    def get(self, request):
        form = addproduct()
        return render(request,"itm/inproduct.html",{"form":form})
    def post(self,request):
        form = addproduct(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            valid_data = data['name']
            # try:
            validator = BalanceStorage.objects.filter(name = valid_data)
            # except:
            #     print("Error")
            product = Inproduct.objects.create(
                name=data['name'],
                inload_number=data['inload_number'],
                count=data['count'],
                unit=data['unit'],
                in_date=data['in_date']
            )
            return redirect("balance")

class Balance(View):
    def get(self,request):
        return render(request,"itm/balancestorage.html")
