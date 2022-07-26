from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(["POST"])
def registerAPI(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    fullname = str(validated_data.get("fullname"))
    username = validated_data.get("username")
    password = validated_data.get("password")
    first_name, last_name = fullname.split(" ")
    if User.objects.filter(username=username).count():
        return Response(
            {
                "detail": "error",
                "data": "An account with this email address already exits",
            }
        )

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

    return Response(
        {
            "detail": "success",
            "data": UserSerializer(user).data,
            "token": Token.objects.get_or_create(user=user)[0].key,
        }
    )


@api_view(["POST"])
def loginAPI(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data["username"]
    password = serializer.validated_data["password"]
    print(username)
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        return Response(
            {
                "detail": "success",
                "user": UserSerializer(user).data,
                "token": Token.objects.get_or_create(user=user)[0].key,
            }
        )
    else:
        return Response(
            {
                "detail": "error",
                "error": "Invalid Username/Password",
            }
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logoutAPI(request):
    try:
        request.user.auth_token.delete()
    except:
        pass
    return Response(
        {
            "detail": "success",
        }
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getUserDetail(request):
    user = request.user
    return Response(
        {
            "detail": "success",
            "data": UserSerializer(user).data,
        }
    )
