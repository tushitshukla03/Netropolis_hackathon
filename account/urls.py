from django.urls import path
from .views import UserList, AuthUserLoginView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("register/", UserList.as_view(), name = "register"),
    path('login/', AuthUserLoginView.as_view(), name = "login"),

]