from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from airports.models import Airport

airport = Airport()


@api_view(['GET'])
def index(request):
    return Response(['INDEX'])


@api_view(['POST'])
def create(request):
    airport.insert(request.data)
    return Response({'message': 'airport_created'}, status.HTTP_200_OK)
