from rest_framework.serializers import ModelSerializer #from tutorial 2
from . models import * #from tutorial 2

class LegislationSerializer(ModelSerializer):
    class Meta:
        model = Legislation
        fields = '__all__'

        