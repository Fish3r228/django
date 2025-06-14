from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'catalog/home.html')

def contacts_view(request):
    return render(request, 'catalog/contacts.html')
##