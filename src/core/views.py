from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'John',
            'age': 23
        }
        return Response(data)

# def test_view(request):
    # data = {
    #     'name': 'John',
    #     'age': 23
    # }
#     return JsonResponse(data, safe=False)