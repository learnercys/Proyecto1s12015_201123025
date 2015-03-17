from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    return Response(['INDEX'], status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    return Response(['CREATE'], status.HTTP_200_OK)

