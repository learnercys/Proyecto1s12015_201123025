from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'GET':
        return Response(['GET'])
    elif request.method == 'POST':
        return Response(['POST'])

@api_view(['DELETE'])
def delete_user(request):
    return Response(['DELETED'])