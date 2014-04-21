from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from taassignment.course import views as course
from taassignment.users import views as user
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', course.public_view_list , name='home'),
    url(r'^admin/', user.staff_view_list, name='staff-home'),
    url(r'^faculty/', course.faculty_view_list, name='faculty-home'),
)

# djangocas
if settings.USE_CAS:
    urlpatterns += patterns('',
        url(r'^accounts/login/$', 'djangocas.views.login', name='account-login'),
        url(r'^accounts/logout/$', 'djangocas.views.logout', name='account-logout'),
        )

    # urlpatterns = patterns('django.views.generic.simple', ('^admin/logout/$', 'redirect_to' ,
    #         {'url': '../../accounts/logout'})) + urlpatterns
# end djangocas

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
