from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name = 'blogpost_list'),
    url(r'^about/$', views.AboutView.as_view(), name = 'about'),
    url(r'^post/(?P<pk>\d+)$', views.BlogPostDetailView.as_view(), name = 'blogpost_detail'),
    url(r'^post/create/$', views.BlogPostCreateView.as_view(), name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.BlogPostUpdateView.as_view(), name = 'blogpost_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.BlogPostDeleteView.as_view(), name = 'blogpost_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name = 'comment_remove'),


]
