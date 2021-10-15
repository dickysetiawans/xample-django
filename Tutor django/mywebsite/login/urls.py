from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^konfirmasi/$',views.konfirmasi),
	url(r'^$', views.index),
]