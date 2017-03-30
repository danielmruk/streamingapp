from django.conf.urls import url
from django.contrib import admin
from ardentlyioapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^stream/sign-in/$', auth_views.login, {'template_name': 'stream/sign_in.html'}, name = 'stream-sign-in'),
    url(r'^stream/sign-out', auth_views.logout, {'next_page': '/'}, name = 'stream-sign-out'),
    url(r'^stream/$', views.stream_home, name = 'stream-home'),
]
