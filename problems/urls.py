from django.conf.urls import patterns, url
from problems import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^data/$', views.data, name='data'),
                       url(r'^user/(?P<name>\w+)/$', views.user, name='user')
                       )
