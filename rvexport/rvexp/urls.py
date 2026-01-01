from django.urls import path
from .views import HomeView, AboutView, ServicesView, PagesView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('pages/', PagesView.as_view(), name='pages'),
    path('contact/', ContactView.as_view(), name='contact'),
]
