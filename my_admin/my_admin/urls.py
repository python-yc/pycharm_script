from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',admin.site.urls),
]
