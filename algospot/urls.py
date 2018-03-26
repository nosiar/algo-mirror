from django.urls import include, re_path

urlpatterns = [
    # Examples:
    # url(r'^$', 'algospot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    re_path(r'^', include(('problems.urls', 'problems'), namespace='problems')),
]
