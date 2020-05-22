from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^delivery/', delivery, name='delivery'),
    url(r'^setup/', setup, name='setup'),
    url(r'^contacts/', contacts, name='contacts'),
]