from django.conf.urls import url

from django.conf import settings

from . import views

from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
]

#urlpatterns += patterns('',
#	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#)

#urlpatterns = [

#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)