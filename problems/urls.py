from django.conf.urls import url
from problems import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^data/$', views.data, name='data'),
    url(r'^user/(?P<name>\w+)/$', views.user, name='user'),
]
