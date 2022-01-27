from rest_framework import serializers
from codenight.models import CodeNight

class CodeNightSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeNight
        fields='__all__'
        read_only_fields=['id']