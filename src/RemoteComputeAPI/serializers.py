from rest_framework import serializers
from .models import FileTest, ExecutableModel


# Serializers translate Django models to JSON fields for use by the API
class FileSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.FileField(max_length=None,
    #                             allow_empty_file=False,
    #                             use_url=False)

    class Meta:
        model = FileTest
        fields = '__all__'


class ExecutableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExecutableModel
        fields = '__all__'
