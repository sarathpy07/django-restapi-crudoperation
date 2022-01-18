from rest_framework.serializers import ModelSerializer
from . models import userapi
class userapiserializer(ModelSerializer):
    class Meta:
        model= userapi
        fields ='__all__'