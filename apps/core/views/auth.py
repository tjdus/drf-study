from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.core.models import User
from apps.core.serializers.auth import SignupSerializer, LoginSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Signup successful!"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(username=serializer.validated_data['username']).first()
            refresh = RefreshToken.for_user(user)
            return Response({
                "accessToken": str(refresh.access_token),
                "refreshToken": str(refresh)
            })
        return Response(serializer.errors, status=400)