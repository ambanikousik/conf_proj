
from .views import *
from django.urls import re_path, include,path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
# from core.view import api_root
#api/product/
urlpatterns =  format_suffix_patterns(  [
   # path('', api_root),

   # User
    re_path(r'^v1/user-list/$', UserList.as_view(), name='user-list'),
    re_path(r'^v1/user-details/$', UserDetails.as_view(), name='user-details'),
   


    
])