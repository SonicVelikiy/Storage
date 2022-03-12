from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Inproduct,Outproduct,BalanceStorage
from .forms import addproduct
from django.views import View
from django.core.paginator import Paginator
from .process import html_to_pdf


def HistoryStorage(request):
    search = request.GET.get("search")
    if search is None:
        inproduct = Inproduct.objects.all()
    else:
        inproduct = Inproduct.objects.filter(name__contains=search)
    return render(request,"itm/addhistory.html",{"inproduct":inproduct})

#bazadan olib yozishga tayyor
class pdf(View):
    def get(self,request):
        pdf = html_to_pdf('itm/inproduct.html')
        return HttpResponse(pdf,content_type='application/pdf')

class CreateProduct(View):
    #mahsulot qo'shish tarixini ishlab chiqish kerak
    def get(self, request):
        form=[1,2,3,4,5,6,7,8,9,10]
        choies=(("kg"),("tonna"),("gramm"),("litr"),("metr"),("sm"),("dona"))
        return render(request, "itm/inproduct.html",{"form":form,"choies":choies})
    def post(self,request):
        number = request.POST.get('number')
        inloadname = request.POST.get('inload')
        outloadname = request.POST.get('outload')
        inloaddate = request.POST.get('date')
        for i in range(1,11):
            mahsulot = "mahsulot" + str(i)
            miqdori = "miqdori" + str(i)
            birlik = "unit" + str(i)
            addmahsulot = request.POST.get(mahsulot)
            addmiqdori = request.POST.get(miqdori)
            addunit = request.POST.get(birlik)

            if addmahsulot and addmiqdori:
                addmahsulot = addmahsulot.lower()
                addmahsulot = addmahsulot.strip()
                try:
                    update = BalanceStorage.objects.get(name=addmahsulot)
                    update.count = update.count + float(addmiqdori)
                    update.save()
                except:
                    BalanceStorage.objects.create(
                        name=addmahsulot,
                        count=addmiqdori,
                        unit=addunit,
                    )
                    product = Inproduct.objects.create(
                        name=addmahsulot,
                        inload_number=number,
                        count=addmiqdori,
                        instorageperson=inloadname,
                        takeinstorageperson=outloadname,
                        unit=addunit,
                        in_date=inloaddate
                    )

            else:
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
