from rest_framework import serializers
from SessionApp.models import Session

class SessionSerializer(serializers.ModelSerializer):  # <-- singulier
    class Meta:
        model = Session
        fields = '__all__'
