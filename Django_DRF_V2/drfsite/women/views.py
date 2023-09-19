from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.response import Response


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer




class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all().values()
        return Response({'posts': list(w)})
        # return Response(WomenSerializer(w, many=True).data)

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post_new': model_to_dict(post_new)})
    
