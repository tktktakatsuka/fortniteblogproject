from django.urls import path 
from .views import BlogList , detailview

urlpatterns = [
    path('detail/<int:pk>/' , detailview , name ='detail'),
    path('', BlogList.as_view() , name ='home'),  
    
]