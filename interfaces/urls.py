from django.urls import path
from .views import home,logic

urlpatterns = [
    path("",home),
    path("generate-excel",logic)
]
