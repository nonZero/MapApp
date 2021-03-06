from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SiteListView.as_view(), name='sites_list'),
    url(r'^add$', views.SiteCreateView.as_view(), name='add_site'),
    url(r'^(?P<pk>\d+)/$', views.SiteDetailView.as_view(), name='view_site'),
    url(r'^(?P<pk>\d+)/edit/$', views.SiteUpdateView.as_view(), name='update_site'),
    url(r'^(?P<pk>\d+)/delete/$', views.SiteDeleteView.as_view(), name='delete_site'),
    url(r'^(?P<site_pk>\d+)/contents/$', views.ContentListView.as_view(), name='content_list'),
    url(r'^(?P<site_pk>\d+)/add-content-from-url/$', views.ContentCreateFromURLView.as_view(),name='create_content_from_url'),
    url(r'^(?P<site_pk>\d+)/add-content/(?P<doc_id>\w+)/$', views.ContentCreateView.as_view(),name='create_content'),
    url(r'^(?P<site_pk>\d+)/(?P<pk>\d+)/$', views.ContentDetailView.as_view(), name='view_content'),
    url(r'^(?P<site_pk>\d+)/(?P<pk>\d+)/edit/$', views.ContentUpdateView.as_view(), name='update_content'),
    url(r'^(?P<site_pk>\d+)/(?P<pk>\d+)/delete/$', views.ContentDeleteView.as_view(), name='delete_content'),
]
