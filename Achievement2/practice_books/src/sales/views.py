from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # protect FBV

# Create your views here.

# define home function
# function takes request from web app
# returns template at sales/home.html as response


def home(request):
    return render(request, 'sales/home.html')


@login_required
def records(request):
    return render(request, 'sales/records.html')
