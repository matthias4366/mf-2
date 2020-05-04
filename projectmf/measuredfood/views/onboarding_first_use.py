from django.shortcuts import render


def nutrientprofile_make_for_user(request):
    """
    To make the application easier for the user, the first nutrient profile
    will be made for them.
    """
    return render(request, 'measuredfood/nutrientprofile_make_for_user.html')
