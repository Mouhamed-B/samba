from .models import Ad, Category
from django.http import Http404
from django.shortcuts import render, reverse
from django.views.generic import DetailView
from .serializers import AdSerializer
import datetime


def index(request):
    template_name = 'advert/index.html'
    context = dict()
    context['i'] = 0
    context['form']=AdSerializer()
    context['categories'] = Category.objects.all()
    context['ads'] = Ad.objects.filter(is_available=True)

    return render(request, template_name, context)


class AdDetail(DetailView):
    """
    View ad detail
    """
    model = Ad
    context_object_name = 'ad'
    template_name = 'advert/ad_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.is_available:
            ads = list()
            for ad in Ad.objects.filter(category__title=self.object.category.title)[:4]:
                if ad != self.object:
                    ads+=[ad]
            
            context['ads'] = ads
            context['breadcrumbs']=[
                {
                    'text':'Samba',
                    'link':reverse('index')
                },
                {
                    'text':self.object.category,
                    'link':''
                },
                self.object.title
            ]
            return context
        else:
            raise Http404