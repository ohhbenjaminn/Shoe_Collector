from django.shortcuts import render

#import the CreateView class
from django.views.generic.edit import CreateView
from django.http import HttpResponse #res.send in express
from .models import Shoe

class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') 

def about(request):
  return render(request, 'about.html') 

def shoes_index(request):
  shoes = Shoe.objects.all() #using our model to get all the rows in our cat table in psql
  return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
  shoe = Shoe.objects.get(id=shoe_id)
  return render(request, 'shoes/detail.html', { 'shoe': shoe })

