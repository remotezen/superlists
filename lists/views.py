from django.shortcuts import render

#  make sure you install lists in settings INSTALLED_APPS
def home_page(request):
    return render(request, 'home.html')
# Create your views here.
