from django.urls import path
from .views import starting_page


urlpatterns = [

       path("" , starting_page , name="starting_page"),



]