from django.conf.urls import url
from . import views

app_name='article'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(),name='home'),
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^archives/$',views.ArchivesView.as_view(),name='archievs'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
]
