from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'qualification', views.QualificationViewSet)
router.register(r'career', views.CareerViewSet)
router.register(r'interests', views.InterestViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]