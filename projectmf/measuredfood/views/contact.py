from django.shortcuts import render


def contact_view(request):
    """
    View displaying an E-Mail address so users can contact me.
    """
    context = {}
    return render(
        request,
        'measuredfood/contact.html',
        context
    )
