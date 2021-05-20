from rest_framework import serializers
from .models import ExecutableModel


class ExecutableSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.FileField(max_length=None,
    #                             allow_empty_file=False,
    #                             use_url=False)

    class Meta:
        model = ExecutableModel
        fields = '__all__'
