from django.urls import path

from apps.core.views.auth import SignupView, LoginView
from apps.core.views.home import HomeView
from apps.core.views.recruitment import RecruitmentListView, RecruitmentDetailView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('auth/signup', SignupView.as_view(), name='signup'),
path('auth/login', LoginView.as_view(), name='login'),
    path('recruitments', RecruitmentListView.as_view(), name='recruitment'),
    path('recruitments/<int:pk>', RecruitmentDetailView.as_view(), name='recruitment_detail'),
]
