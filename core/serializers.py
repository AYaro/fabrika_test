from fabrika.base import BaseModelSerializer
from .models import App
from rest_framework import serializers

class AppSerializer(BaseModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class UpdateAppSerializer(BaseModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

    def validate(self, attrs):
        unknown =  set(self.initial_data) - set(self.fields)
        if unknown:
            raise serializers.ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        if self.initial_data.get('api', None):
            raise serializers.ValidationError("Changing api is not allowed")
        return attrs

    api = serializers.CharField(read_only=True)

class AppAPISerializer(BaseModelSerializer):
    class Meta:
        model = App
        fields = ('api',)