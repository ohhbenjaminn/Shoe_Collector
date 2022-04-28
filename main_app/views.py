from django.shortcuts import render, redirect

#import the CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponse #res.send in express
from .models import Shoe, Accessory
from .forms import ReleaseForm

class ShoeCreate(CreateView):
  model = Shoe
  fields = ['name', 'brand', 'description', 'size']
  # '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['brand', 'description', 'size']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') 

def about(request):
  return render(request, 'about.html') 

def shoes_index(request):
  shoes = Shoe.objects.all() #using our model to get all the rows in our cat table in psql
  return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    accessories_shoe_doesnt_have = Shoe.objects.exclude(id__in = shoe.accessories.all().values_list('id'))
    release_form = ReleaseForm()

    return render(request, 'shoes/detail.html', {'shoe': shoe, 'release_form': release_form,
    'accessories': accessories_shoe_doesnt_have    
    })

def add_release(request, shoe_id):
	form = ReleaseForm(request.POST)
	if form.is_valid():
		new_release = form.save(commit=False)
		new_release.shoe_id = shoe_id
		new_release.save() 

	return redirect('detail', shoe_id=shoe_id)

def assoc_accessory(request, shoe_id, accessory_id):
  Shoe.objects.get(id=shoe_id).accessories.add(accessory_id)
  return redirect('detail', shoe_id=shoe_id)

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'