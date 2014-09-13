from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<user_id>[0-9]+)/edit/update/$', views.update, name='update'),
    url(r'^add/create/$', views.create, name='create'),
    url(r'^(?P<user_id>[0-9]+)/delete/$', views.delete, name='delete'),

]
