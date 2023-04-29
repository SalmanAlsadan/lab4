from django.urls import path 
from . import views
urlpatterns = [
    path("",views.view1,name="tax"),
    path("<int:number>", views.view2,name="number"),
    path("taxrate",views.view3,name="rate")
    ]