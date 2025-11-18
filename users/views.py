from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer




class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile