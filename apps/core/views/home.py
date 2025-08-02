from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"userId": "1", "name":"name"})

    def post(self, request):
        return Response({"message": "Hello, world!"})

    def patch(self, request):
        return Response({"message": "Hello, world!"})

    def put(self, request):
        return Response({"message": "Hello, world!"})

    def delete(self, request):
        return Response({"message": "Hello, world!"})