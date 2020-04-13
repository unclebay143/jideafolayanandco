from django.urls import path
from .views import Maintain, Home, About, Ourwork, Testimony, Team, Contact, Services, Internship


urlpatterns = [
path('maintain', Maintain, name="maintain"),
path('', Home, name="index"),
path('about/', About, name="about"),
path('ourwork', Ourwork, name="ourwork"),
path('testimony', Testimony, name="testimony"),
path('contact/', Contact, name="contact"),
path('team', Team, name="team"),
path('services', Services, name="services"),
path('internship', Internship, name="internship"),

]
