from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Application
from apps.core.serializers.application import ApplicationSerializer, ApplicationDetailSerializer


class ApplicationListView(APIView):
    def get(self, request):
        applications = Application.objects.all().prefetch_related("application_field_set", "applicant")
        serializer = ApplicationDetailSerializer(applications, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        user = request.user
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save(applicant=user)
            return Response(ApplicationDetailSerializer(application).data, status=201)
        return Response(serializer.errors, status=400)

class ApplicationRecruitmentDetailView(APIView):
    def get(self, request, recruitment_id):
        applications = Application.objects.filter(recruitment_id=recruitment_id).prefetch_related("application_field_set")
        serializer = ApplicationDetailSerializer(applications, many=True)
        return Response(serializer.data, status=200)


class ApplicationDetailView(APIView):
    def get_object(self, pk):
        return Application.objects.get(pk=pk)

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationDetailSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            application = serializer.save()
            return Response(ApplicationDetailSerializer(application).data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=204)