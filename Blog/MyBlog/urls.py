from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^gbook/(?P<pageNumber>\d+)/$', views.gbook, name='gbook'),
    url(r'^learn/', views.learn, name='learn'),
    url(r'^manshenghuo/', views.manshenghuo, name='manshenghuo'),
    url(r'^mbfx/', views.mbfx, name='mbfx'),

    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^checkaccount/', views.checkAccount, name='checkAccount'),
    url(r'^checkpassword/', views.checkPassword, name='checkPassword'),
    url(r'^checkusername/', views.checkUsername, name='checkUsername'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^collection/', views.collection, name='collection'),
    url(r'^addcollection/(?P<collection>\w+)/(?P<path>\w+)/$',
        views.addCollection, name='addCollection'),
    url(r'^delcollection/(?P<collection>\w+)/$', views.delCollection,
        name='delCollection'),
    url(r'^comment/', views.comment, name='comment'),
]
