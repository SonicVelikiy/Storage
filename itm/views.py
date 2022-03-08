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
    return render(request,"itm/addhistory.html",{"inproduct":inproduct})

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
            validator = BalanceStorage.objects.get(name=valid_data)
            if not (validator):
                BalanceStorage.objects.create(
                    name=data['name'],
                    count=data['count'],
                    unit=data['unit'],
                )
            else:
                update = BalanceStorage.objects.get(name=valid_data)
                update.count = update.count+float(data['count'])
                update.save()
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
        search = request.GET.get('search')
        if search is None:
            data = BalanceStorage.objects.all()
            search=""
        else:
            data = BalanceStorage.objects.filter(name__contains=search)

        return render(request,"itm/balancestorage.html",{"data":data,"search":search})
