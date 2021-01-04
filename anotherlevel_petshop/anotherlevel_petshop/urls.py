##from django.contrib import admin
##from django.urls import path
##
##urlpatterns = [
##    path('admin/', admin.site.urls),
##]

# When you enter /admin/ in url, django admin is run.

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('polls.urls')),
    url(r'^', include('blog.urls')),
]
