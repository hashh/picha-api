from rest_framework import serializers
from photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['fulfilled_on', 'created_on', 'title', 'link', 'image_url', 'description']