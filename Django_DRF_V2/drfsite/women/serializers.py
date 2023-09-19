from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField() 
    time_create = serializers.DateTimeField(read_only=True) 
    time_update = serializers.DateTimeField(read_only=True) 
    is_published = serializers.BooleanField(default=True) 
    cat_id = serializers.IntegerField()

    
# def encode():
#     model = WomenModel('title: Saspence', 'content: Hello World')
#     model_ser = WomenSerializer(model)
#     print(model_ser.data, type(model_ser.data), sep='\n')
#     json = JSONRenderer().render(model_ser.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title": "Saspence", "content": "Hello World"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = '__all__'