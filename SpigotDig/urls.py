
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^stateselect/', include('stateselect.urls')),
    url(r'^admin/', admin.site.urls),
]
