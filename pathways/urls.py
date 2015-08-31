from django.conf.urls import url
from pathways import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^subjects/(?P<industry_pk>\d+)/$', views.subjects, name='subjects'),
]