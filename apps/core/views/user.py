from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Recruitment, User
from apps.core.serializers.recruitment import RecruitmentDetailSerializer


## 유저가 작성한 모집글을 조회하는 API
class UserRecruitmentListView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        recruitments = Recruitment.objects.filter(created_by=user).select_related("created_by").prefetch_related("recruitment_field_set__field")
        serializers = RecruitmentDetailSerializer(recruitments, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)
