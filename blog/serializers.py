from rest_framework import serializers
from blog.models import Posts

class PostSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {
            'url':{'title', 'category'},

        }


