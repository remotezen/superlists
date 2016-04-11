from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError
from django.utils.html import escape

#  make sure you install lists in settings INSTALLED_APPS


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = escape("You can't have an empty list item")
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id,))


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id,))
        except ValidationError:
            error = "You can't have an emtpy list item"

    return render(request, 'list.html', {'list': list_, 'error': error})
# Create your views here.


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id,)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
