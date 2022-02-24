from django.urls import path
from .views import home,add,edit,delete,update,VehicleDetail
urlpatterns = [
    path('',home),
    path('add/',add),
    path('update/',update),
    path('edit/<slug:slug>',edit),
    path('delete/<slug:slug>',delete),
    path('detail/<slug:slug>',VehicleDetail.as_view()),  
      
]
