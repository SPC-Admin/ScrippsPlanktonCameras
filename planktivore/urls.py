from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'planktonview2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^data/admin/', admin.site.urls),
    url(r'^data/rois/', include('rois.urls')),
    url(r'^data/roistats/',include('roistats.urls')),
    url(r'^data/api-auth/',include('rest_framework.urls', namespace='rest_framework'))
]
