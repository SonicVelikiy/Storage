from django.contrib import admin
from .models import Inproduct,Outproduct,BalanceStorage

admin.site.register(Inproduct)
admin.site.register(Outproduct)
admin.site.register(BalanceStorage)
