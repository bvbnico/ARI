from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    #url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='device_post'),
    #url(r'^books/$', views.BookListView.as_view(), name='books'),
    #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    #path('informacion/', views.devices_posts, name='device_post'),
    path('general/', views.users_view, name='user_view')
]
