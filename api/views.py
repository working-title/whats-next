from rest_framework import viewsets

from pathways.models import Qualification, Career, Interest
from api.serializers import QualificationSerializer, CareerSerializer, InterestSerializer


class QualificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows qualifications to be viewed.
    """
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class CareerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows careers to be viewed.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class InterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interests to be viewed.
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
