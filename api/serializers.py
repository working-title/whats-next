from rest_framework import serializers
from pathways.models import Qualification, Career, Interest


class QualificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Qualification
        fields = ('name', 'debt')

class CareerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Career
        fields = ('name',
                  'income',
                  'qualifications',
                  'maori_name',
                  'hours_worked_30_less',
                  'hours_worked_60_less',
                  'hours_worked_60_more')

class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = ('name',
                  'careers',
                  'maori_name')
