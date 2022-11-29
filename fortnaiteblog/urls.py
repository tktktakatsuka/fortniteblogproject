from django.urls import path
from .views import BlogList , detailview , google , countDownView

urlpatterns = [
    path('detail/<int:pk>/' , detailview , name ='detail'),
    path('countDown' , countDownView , name ='countDown'),
    path('google78b143064e223f8d.html/', google, name='google'),
    path('', BlogList.as_view() , name ='home'),

]