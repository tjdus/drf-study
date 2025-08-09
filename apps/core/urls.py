from django.urls import path

from apps.core.views.application import ApplicationListView, ApplicationDetailView, ApplicationRecruitmentDetailView
from apps.core.views.auth import SignupView, LoginView
from apps.core.views.home import HomeView
from apps.core.views.recruitment import RecruitmentListView, RecruitmentDetailView
from apps.core.views.user import UserRecruitmentListView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('auth/signup', SignupView.as_view(), name='signup'),
path('auth/login', LoginView.as_view(), name='login'),
    path('recruitments', RecruitmentListView.as_view(), name='recruitment'),
    path('recruitments/<int:pk>', RecruitmentDetailView.as_view(), name='recruitment_detail'),
    path('applications', ApplicationListView.as_view(), name='application_list'),
    path('applications/<int:pk>', ApplicationDetailView.as_view(), name='application_detail'),
    path('applications/recruitments/<int:recruitment_id>', ApplicationRecruitmentDetailView.as_view(), name='application_recruitment_detail'),
    path("users/<int:pk>/recruitments", UserRecruitmentListView.as_view(), name="user_recruitment_list"),
]
