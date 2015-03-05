from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User

# we cannot try to load the database user. To slow.
user = User()


@api_view(['POST'])
def create(request):
    return Response(['CREATE'])


@api_view(['DELETE'])
def delete(request):
    return Response(['DELETED'])


@api_view(['GET'])
def get(request):
    return Response(user.get_all())

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
