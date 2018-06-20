from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^index/', include('index.urls')),
    url(r'^admin/', admin.site.urls),
]
