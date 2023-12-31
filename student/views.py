from django.contrib.auth import authenticate
from pprint import pprint

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from drf_yasg.utils import no_body, swagger_auto_schema


from .renderers import UserRenderer
from .models import Student
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserChangePasswordSerializer, SendPasswordResetEmailSerializer, \
    UserPasswordResetSerializer, LogoutSerializer


""" Viewsets for User Authentication """
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'message': "Ro'yhatdan muvaffaqiyatli o'tdingiz"}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            active_user = Student.objects.get(id=user.id)
            serializer = UserProfileSerializer(active_user)
            return Response({
                'token': token,
                'user_profile_data': serializer.data,
                'message': 'Tizimga muvaffaqiyatli kirdingiz',
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'errors': {
                    'non_field_errors': ["Kiritilgan 'parol' yoki 'email' noto'g'ri"]
                }
            }, status=status.HTTP_404_NOT_FOUND)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Parol muvaffaqiyatli o'zgartirildi"}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Parolni tiklash uchun link yuborildi. Iltimos emailingizni tekshiring"}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Parol muvaffaqiyatli yangilandi'}, status=status.HTTP_200_OK)

""" Student profil viewset """
class UserProfileView(viewsets.ModelViewSet):
    """ Student profile ma'lumotlarini beruvchi viewset """
    queryset = Student.objects.filter(status=True)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    @swagger_auto_schema(request_body = no_body) # ishlamayapdi 🔴
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, format=None, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        student_data = self.get_object()
        data = request.data

        try:
            if Student.objects.filter(email=data['email']) and student_data.email != data['email']:
                return Response({'error': "Bunday 'email' avval yaratilgan ! Iltimos boshqa 'email' tanlang."}, status=status.HTTP_204_NO_CONTENT)
        except: 
            pass

        try:
            student_data.password = data['password'] if 'password' in data else student_data.password
            student_data.email = data['email'] if 'email' in data else student_data.email
            student_data.first_name = data['first_name'] if 'first_name' in data else student_data.first_name
            student_data.last_name = data['last_name'] if 'last_name' in data else student_data.last_name
            student_data.ball = data['ball'] if 'ball' in data else student_data.ball
            student_data.coin = data['coin'] if 'coin' in data else student_data.coin
            student_data.phone = data['phone'] if 'phone' in data else student_data.phone

            student_data.save()
            serializer = UserProfileSerializer(student_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'errors': "Ma'lumotlarni saqlashda xatolik sodir bo'ladi!!!"}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

"""  Viewsets for other models  """
# class ContactViewset(viewsets.ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     permission_classes = [AllowAny]

# class StudentViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.filter(status=True)
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]




