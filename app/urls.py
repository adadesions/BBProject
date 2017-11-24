from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^more-register/$', views.more_register, name='more_register'),
]
