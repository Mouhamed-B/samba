from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Vue de la page index
    """

    return render(request, template_name='frontend/index.html')