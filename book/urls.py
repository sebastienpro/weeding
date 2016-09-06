from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_page$', views.add_page, name='add_page'),
    url(r'^page_edit/(?P<page_id>\d+)/?$', views.page_edit, name='page_edit'),
    url(r'^preview/(?P<page_id>\d+)/$', views.preview, name='preview'),
    url(r'^photos/$', views.photos, name='photos'),
]