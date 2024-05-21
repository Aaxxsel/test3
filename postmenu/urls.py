from django.urls import path
from postmenu.views import *

urlpatterns = [
    path('', create_post, name='create_post'),
    path('posts/', listpost, name='list_post'),
]
