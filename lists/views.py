from django.shortcuts import render, redirect
from lists.models import  Item

#  make sure you install lists in settings INSTALLED_APPS


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
# Create your views here.
