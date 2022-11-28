from django.urls import path
from .views import BlogList , detailview , google

urlpatterns = [
    path('detail/<int:pk>/' , detailview , name ='detail'),
    path('', BlogList.as_view() , name ='home'),
    path('google78b143064e223f8d.html/', google, name='google'),
]