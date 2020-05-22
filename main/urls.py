from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^delivery/', delivery, name='delivery'),
    url(r'^setup/', setup, name='setup'),
    url(r'^contacts/', contacts, name='contacts'),
    url(r'^sale/', sale, name='sale'),
    url(r'^search/', search, name='search'),
    path('category/<int:pk>/', category, name='category'),
]