from django.conf.urls import include, url
from django.contrib import admin
import blog.models 

print admin.site.urls
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'task1.views.home', name='home'),
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
