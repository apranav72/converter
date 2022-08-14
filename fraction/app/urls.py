from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('fraction', views.fractionS, name='fractionss'),
	path('about', views.about, name='about'),
]
