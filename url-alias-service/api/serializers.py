from rest_framework import serializers

from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = '__all__'
        read_only_fields = ('short_id', 'created_at', 'expires_at')


class ShortLinkStatsSerializer(serializers.Serializer):
    short_id = serializers.CharField()
    original_url = serializers.URLField()
    clicks = serializers.IntegerField()
