from django.shortcuts import render
from django.http import HttpResponse

#  make sure you install lists in settings INSTALLED_APPS


def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
# Create your views here.
