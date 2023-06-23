
from django.urls import path
from ecommapp import views
from ecommapp.views import SimpleView
urlpatterns = [
    path("about", views.about),
    path("contact", views.contact),
    path("home", views.home),
    path("edit/<rid>", views.edit),
    path('delete/<rid>', views.delete),
    path("myview",SimpleView.as_view()),
    path('hello', views.hello),
    
   

]
