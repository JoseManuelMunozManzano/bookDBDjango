from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.book_list),
	url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
	url(r'^author/(?P<pk>[0-9]+)/$', views.book_author, name='book_author'),
	url(r'^book/new/$', views.book_new, name='book_new'),
	url(r'^book/(?P<pk>[0-9]+)/edit/$', views.book_edit, name='book_edit'),
]
