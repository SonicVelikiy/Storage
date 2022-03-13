from django.urls import path
from .views import InHistory,CreateProduct,Balance,pdf,KickProduct,OutHistory

urlpatterns = [
    path("",Balance.as_view(),name="balance"),
    path("inhistory/",InHistory,name="inhistory"),
    path("outhistory/",OutHistory,name="outhistory"),
    path("addproduct/",CreateProduct.as_view(),name="inproduct"),
    path("kickproduct/",KickProduct.as_view(),name="kickproduct"),
    path("pdf/",pdf.as_view())
]