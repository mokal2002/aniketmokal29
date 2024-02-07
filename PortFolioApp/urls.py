from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="PortFolioApp"),
   path("contact/", views.contact, name="contact"),
   path("feedback/", views.feedback, name="feedback"),
   

    
]
