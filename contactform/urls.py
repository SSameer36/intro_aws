from django.contrib import admin
from django.urls import path
from contactform.views import ContactView
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('',ContactView.as_view()),
    path('thanks/', cache_page(60*60)(TemplateView.as_view(template_name='thanks.html')), name="Thanks" )

]