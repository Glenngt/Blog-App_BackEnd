from rest_framework import serializers
from add_post.models import AddPostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta :
        model = AddPostModel
        fields = (
            'userid',
            'title',
            'msg'
        )