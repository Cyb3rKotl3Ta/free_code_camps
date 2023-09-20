from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser




# equals to WomenSerializer(serializers.Serializer) that above al this code
class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta: 
        model = Women
        fields = '__all__'










# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

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





# class WomenSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField() 
    # time_create = serializers.DateTimeField(read_only=True) 
    # time_update = serializers.DateTimeField(read_only=True) 
    # is_published = serializers.BooleanField(default=True) 
    # cat_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title) 
    #     instance.content = validated_data.get('content', instance.content) 
    #     instance.is_published = validated_data.get('is_published', instance.is_published) 
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id) 
    #     instance.save() 
    #     return instance

    
