from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User, Auth

# we cannot try to load the database user in each request. To slow.
# once the server was started, the unique way to update the users tree
# is by a creates --> create user request to be exactly. Same thing
# to auth session.
user = User()
auth = Auth()


@api_view(['GET'])
def index(request):
    return Response(['INDEX'])


@api_view(['POST'])
def create(request):
    if user.find(request.data):
        return Response({'message': 'user_already_exist'}, status.HTTP_400_BAD_REQUEST)

    user.insert(request.data)
    # if the user is created we verify the avl tree to know if it's necessary
    # to re-order.
    return Response({'message': 'user_created'}, status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request):
    return Response(['DELETED'])


@api_view(['GET'])
def get(request):
    return Response(user.get_all())


@api_view(['POST'])
def login(request):
    _user = user.find(request.data)
    if _user is not None and _user.data.get('password') == request.data.get('password'):

        return Response(
            {
                'message': 'login_created',
                'token': auth.save_token(request.data.get('username'))
            }, status.HTTP_200_OK
        )

    return Response({'message': 'cannot_login'}, status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def logout(request):
    return Response({
        'data': []
    })


@api_view(['GET'])
def profile(request):
    return Response([])
