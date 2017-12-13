from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^gbook/', views.gbook, name='gbook'),
    url(r'^learn/', views.learn, name='learn'),
    url(r'^manshenghuo/', views.manshenghuo, name='manshenghuo'),
    url(r'^mbfx/', views.mbfx, name='mbfx'),

    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
]
