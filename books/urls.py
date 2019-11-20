from django.urls import path,re_path
from django.conf.urls import url
from .views import current_url_view,search

urlpatterns=[
path('',current_url_view),
#path('search-form/', search_form),
path('search/',search),

]