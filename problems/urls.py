from django.urls import re_path
from problems import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^data/$', views.data, name='data'),
    re_path(r'^user/(?P<name>\w+)/$', views.user, name='user'),
]
