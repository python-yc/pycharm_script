from django.conf.urls import include, url
from django.contrib import admin

# from teach_session import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'teach_session.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',admin.site.urls),

    # url(r'^sess/',v.mySession),
    # url(r'^stu/',v.StudentListView.as_view())
]

