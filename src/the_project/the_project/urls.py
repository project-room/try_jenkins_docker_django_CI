from django.conf.urls import url, include
from django.contrib import admin

from the_project.welcome import welcome

urlpatterns = [
    url(r'^welcome/$', welcome),
    url(r'^admin/', admin.site.urls),
]
