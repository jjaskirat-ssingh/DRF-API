# from django.http import JsonResponse
from django.shortcuts import render

# DRF Imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

# def test_view(request):
#     data = {
#         'name': 'John Doe',
#         'age': 23
#     }
#     return JsonResponse(data)

# class TestView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         # post = qs.first() 
#         serializer = PostSerializer(qs, many=True)
#         # serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# The following three classes provide the same functionality but varied code length. 

class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):    

    permission_classes = (IsAuthenticated, )

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
        
    # def perform_create(self, serializer):
    #     # send an email
    #     serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):

    permission_classes = (IsAuthenticated, )
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
