from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.book_list),
	url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
]
