from django.conf.urls import url

from pathways import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]