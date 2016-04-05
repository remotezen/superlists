from django.shortcuts import render, redirect
from lists.models import  Item, List

#  make sure you install lists in settings INSTALLED_APPS


def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' %( list_.id,))


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list' : list_})
# Create your views here.

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id,)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
