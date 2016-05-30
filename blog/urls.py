from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^tweet/$', views.tweet, name='tweet'),
    url(r'^tweet_list/$', views.tweet_list, name='tweet_list'),
]
