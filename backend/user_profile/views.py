from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Profile
from .serializers import GetUserProfileSerializer


class GetUserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserProfileSerializer

    def get(self, request: Request):
        user_profile = Profile.objects.get(user_id=request.user.id)
        serializer = self.serializer_class(instance=user_profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EditUserProfileAPIView(APIView):
    ...
