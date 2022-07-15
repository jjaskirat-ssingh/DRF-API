from django.http import JsonResponse
from django.shortcuts import render

# DRF Imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'John Doe',
            'age': 23
        }     
        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'John Doe',
#         'age': 23
#     }
#     return JsonResponse(data)

