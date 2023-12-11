from django.shortcuts import render, redirect

# django authentication libraries
from django.contrib.auth import authenticate, login, logout
# django form for auth
from django.contrib.auth.forms import AuthenticationForm


# function to login


def login_view(request):
    error_message = None
    # Create form object
    form = AuthenticationForm()

    # when user hits login button and generates POST request
    if request.method == 'POST':
        # read data sent by form via POST
        form = AuthenticationForm(data=request.POST)

    # check if form is valid
    if form.is_valid():
        username = form.cleaned_data.get('username')  # read username
        password = form.cleaned_data.get('password')  # read password

    # use Django authenticate function to validate user
        user = authenticate(username=username, password=password)
    # user authenticated
        if user is not None:
            # login user
            login(request, user)
        # send user to desired page
            return redirect('recipe:recipe_list')
        else:
            error_message = 'Something went wrong'

    # prepare data to send from view to template
    context = {
        'form': form,  # send form data
        'error_message': error_message  # send error message
    }

    # load the login page
    return render(request, 'auth/login.html', context)


# function to logout
def logout_view(request):
    logout(request)
    return redirect('logout_success')


def logout_success(request):
    return render(request, 'auth/success.html')
