from .models import Ad, Category
from django.http import Http404
from django.shortcuts import render, reverse
from django.views.generic import DetailView
from .serializers import AdSerializer


def index(request):
    template_name = 'advert/index.html'
    context = dict()
    context['i'] = 0
    context['form']=AdSerializer()
    context['categories'] = Category.objects.all()
    context['ads'] = Ad.objects.all()

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