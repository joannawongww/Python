from django.shortcuts import render

# Create your views here.

# define home function
# function takes request from web app
# returns template at sales/home.html as response


def home(request):
    return render(request, 'sales/home.html')
