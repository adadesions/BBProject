from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns = [
    url('', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('more-register/', views.more_register, name='more_register'),
    url('marathon-exercise/', views.marathon, name='marathon'),
]
