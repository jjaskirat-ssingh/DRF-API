# from django.http import JsonResponse
from django.shortcuts import render

# DRF Imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post

# def test_view(request):
#     data = {
#         'name': 'John Doe',
#         'age': 23
#     }
#     return JsonResponse(data)

class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # post = qs.first() 
        serializer = PostSerializer(qs, many=True)
        # serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)