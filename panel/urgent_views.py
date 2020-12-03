from .models import Profile
from .tests import is_staff
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from advert.models import Ad, Category

from django.contrib import messages

def index(request,usr):
    """
    Page utilisateur
    """
    template_name = 'panel/index.html'
    context=dict()
    try:
        user = User.objects.get(username=usr)
        context['user']=user
        assert (request.user==user)
        context['self']=True
    except User.DoesNotExist:
        raise Http404("Cet utilisateur n'existe pas")
    except AssertionError:
        context['self']=False
    context['categories'] = Category.objects.all()    
    context['breadcrumbs']=[
        {
            'text':'Samba',
            'link':reverse('index')
        },
        {
            'text':'Profil',
            'link':request.path
        },
        user.username
    ]
    return render(request, template_name,context)


def panel(request):
    if request.user.is_staff:
        template_name = 'panel/admin.html'
        context = dict()
        
        #context['users'] = User.objects.all()
        #context['std_profiles'] = Profile.objects.filter(has_company=False)
        #context['pro_profiles'] = Profile.objects.filter(has_company=True)
        context['i']=0
        context['categories'] = Category.objects.all() 

        return render(request, template_name, context)
    else:
        raise Http404

def loginPage(request):
	if request.user.is_authenticated:
		raise Http404
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')
		return redirect('index')