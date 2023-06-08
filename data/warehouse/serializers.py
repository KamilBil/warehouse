from rest_framework import serializers
from rest_framework.fields import Field
from .models import Group, Post
import re

class GroupSerializer(serializers.Serializer):
    external_id = serializers.IntegerField()
    name = serializers.CharField()
class PostSerializer(serializers.Serializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    added_in_social_media = serializers.CharField(write_only=True)
    text_value = serializers.CharField()
    group_id = serializers.IntegerField(write_only=True)
    label = serializers.CharField(read_only=True)
    external_id = serializers.CharField()
    def save(self):
        g, created = Group.objects.update_or_create(external_id=self.validated_data["group_id"])
        p, created = Post.objects.update_or_create(
            external_id=self.validated_data["external_id"],
            defaults={
                'group_id': g.pk,
                'text_value' : self.validated_data["text_value"],
                'external_id' : self.validated_data["external_id"],
                'added_in_social_media':self.extract_date(self.validated_data["added_in_social_media"])
            }
        )

    @staticmethod
    def extract_date(date_str: str):
        match = re.search(r'\b\d{4}-\d{2}-\d{2}\b', date_str)
        if match:
            return match.group()
        return None
