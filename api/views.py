import json
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from pathways.models import Qualification, Career, Interest, Industry
from api.serializers import QualificationSerializer, CareerSerializer, InterestSerializer, IndustrySerializer


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


class IndustryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows industries to be viewed.
    """
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    parser_classes = (JSONParser,)

    @list_route(methods=['post'], url_path='from_tags')
    def from_tags(self, request, pk=None):
        """
        Gets the first 3 industries that match the tags posted.
        """

        if not request.data:
            return Response({'error': "There was no JSON data posted."})

        try:
            tags = request.data['tags']

            if len(tags) == 0:
                return Response({'error': "Expected at least one tag."})
        except KeyError:
            return Response({'error': "Expected a JSON list of tags to find industries with under the key 'tags'"})

        # get first 3 industries that have the tags that were posted.
        # make sure they're distinct so we don't get multiple results if the same
        # model matches two or more tags
        industries = Industry.objects.filter(tags__name__in=tags).distinct()[:3]

        if len(industries) == 0:
            return Response({'error': "No industries matched the given tags."})

        serializer = IndustrySerializer(industries, many=True)
        return Response(serializer.data)


class InterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interests to be viewed.
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
