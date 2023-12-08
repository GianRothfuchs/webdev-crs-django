from django.urls import path 
from . import views 

# this refers to the fiel views.py, which contains a
# function called index, hence views.index, name is just a naming
urlpatterns = [ 
    path('', views.index, name='index'), 
] 