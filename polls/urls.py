from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    # ex: /5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]