from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServicesView(TemplateView):
    template_name = 'service.html'

class PagesView(TemplateView):
    template_name = 'pages.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
