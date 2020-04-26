from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'measuredfood/home.html')


def initial_tutorial_1(request):
    """
    When the user first opens the application, they are shown a tutorial to
    guide them threw the application.
    """
    return render(request, 'measuredfood/initial_tutorial_1.html')
