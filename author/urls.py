from django.urls import path
from .views import starting_page,author_register


urlpatterns = [

       path("" , starting_page , name="starting_page"),
       path("register/" , author_register , name="author_register"),



]