from rest_framework import serializers
from machinlearningmodel.models import Clasiffier

class ClasiffierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasiffier
        fields = ('id', 'texto')