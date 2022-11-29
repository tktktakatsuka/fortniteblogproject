import datetime
from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel

# Create your views here.
def detailview(request , pk):
    object = BlogModel.objects.get(pk=pk)
    return render(request, 'detail.html' ,{'object' : object})

# Create your views here.
class BlogList(ListView):
    template_name = 'home.html'
    model = BlogModel
    paginate_by = 3

# Create your views here.
def google(request):
    return render(request, 'google78b143064e223f8d.html')

# Create your views here.
def countDownView(request):
    dt_now = datetime.datetime.now()
    time_left = dt_now + datetime.timedelta(minutes=90)
    strftime_time_left = time_left.strftime('%B %d,%Y %H:%M:%S')
    context = {
    'time_left': strftime_time_left
    }
    return render(request, 'countDown.html', context)
 
