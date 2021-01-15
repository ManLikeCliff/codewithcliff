from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .models import Contact
from django.http import HttpResponse


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['clients'] = Client.objects.all()
        return context

    def home(request):
        if request.method=="POST":
            contact=Contact()
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            contact.name=name
            contact.email=email
            contact.message=message
            contact.save()
            return HttpResponse("<strong>Message delivered successfully, I'll be in touch the very soonest</strong>")
        return render(request, 'home.html')
