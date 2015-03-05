from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def create(request):
    return Response(['CREATE'])


@api_view(['DELETE'])
def delete(request):
    return Response(['DELETED'])


@api_view(['POST'])
def login(request):
    return Response({
        'data': []
    })


@api_view(['DELETE'])
def logout(request):
    return Response({
        'data': []
    })


@api_view(['GET'])
def profile(request):
    return Response([])
