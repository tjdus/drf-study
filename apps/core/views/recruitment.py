from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Recruitment
from apps.core.serializers.recruitment import RecruitmentSerializer, RecruitmentDetailSerializer


class RecruitmentListView(APIView):
    def get(self, request):
        serializer = RecruitmentDetailSerializer(Recruitment.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecruitmentSerializer(data=request.data)
        if serializer.is_valid():
            recruitment = serializer.save(created_by=request.user)
            return Response(RecruitmentSerializer(recruitment).data, status=201)
        return Response(serializer.errors, status=400)

class RecruitmentDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(
            Recruitment.objects.select_related('created_by'),  # 예시: created_by가 User 모델을 참조
            pk=pk
        )

    def get(self, request, pk):
        recruitment = self.get_object(pk)
        serializer = RecruitmentDetailSerializer(recruitment)
        return Response(serializer.data)

    def put(self, request, pk):
        recruitment = self.get_object(pk)

        serializer = RecruitmentSerializer(recruitment, data=request.data)
        if serializer.is_valid():
            recruitment = serializer.save()
            return Response(RecruitmentDetailSerializer(recruitment).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        recruitment = self.get_object(pk)
        recruitment.delete()
        return Response(status=204)