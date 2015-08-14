from rest_framework import serializers
from rest_framework.exceptions import ParseError
from pathways.models import Qualification, Career, Interest, Industry


class TagListSerializer(serializers.Field):
    """
    Used to serialize tags made with the taggit library.
    """

    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_representation(self, value):
        if type(value) is not list:
            return [tag.name for tag in value.all()]
        return value


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('name', 'debt')


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('name',
                  'income',
                  'qualifications',
                  'maori_name',
                  'hours_worked_30_less',
                  'hours_worked_60_less',
                  'hours_worked_60_more',
                  'no_qualification',
                  'school',
                  'post_school',
                  'degree')
        depth = 2


class IndustrySerializer(serializers.ModelSerializer):
    tags = TagListSerializer()

    class Meta:
        model = Industry
        fields = ('name',
                  'description',
                  'careers',
                  'tags',)
        depth = 2


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name',
                  'careers',
                  'maori_name')
        depth = 2



