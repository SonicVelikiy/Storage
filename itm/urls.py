from django.urls import path
from .views import HistoryStorage,CreateProduct,Balance,pdf

urlpatterns = [
    path("",Balance.as_view(),name="balance"),
    path("history",HistoryStorage,name="history"),
    path("addproduct/",CreateProduct.as_view(),name="inproduct"),
    path("pdf/",pdf.as_view())
]