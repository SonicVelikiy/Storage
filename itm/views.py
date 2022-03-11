from django.shortcuts import render, redirect
from .models import Inproduct,Outproduct,BalanceStorage
from .forms import addproduct
from django.views import View
from django.core.paginator import Paginator

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
            try:
                validator = BalanceStorage.objects.get(name=valid_data)
                update = BalanceStorage.objects.get(name=valid_data)
                update.count = update.count + float(data['count'])
                update.save()
            except:
                BalanceStorage.objects.create(
                    name=data['name'],
                    count=data['count'],
                    unit=data['unit'],
                )
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
            paginator = Paginator(data,15)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)
            search=""
        else:
            data = BalanceStorage.objects.filter(name__contains=search)
            paginator = Paginator(data,15)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)

        return render(request,"itm/balancestorage.html",{"search":search,"page":page_obj,"all":paginator})
