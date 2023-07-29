# django modules
from django.shortcuts import render

# rest framework modules
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.throttling import UserRateThrottle

# local modules
from .models import CourseCategory, Course,  Unit, Lessons, File, Teacher, MyCourse
from .serializers import  CourseCategory_APISerializer, Courses_for_Category_APISerializer,   Course_APISerializer, Unit_APISerializer, \
    Lesson_APISerializer, Teachers_list_APISerializer,  Teacher_APISerializer, MyCourse_APISerializer, MyCourse_GET_APISerializer

from student.models import Student

# Create your views here.
"""
TO DO:
CourseCategory_Viewset ✔
Course_Viewset ✔
Unit_Viewset ✔
LessonViewset ✔
Teacher_Viewset ✔
MyCourseViewSet ♻

"""

""" ------------------------------------------------------------------------------   
                                 Courses Section 
---------------------------------------------------------------------------------- """

class CourseCategory_Viewset(ModelViewSet):
    """ Kurslarning kategoriyasi uchun viewset
    faqat list(GET) ishlaydi, qolgan metodlarga ruhsat yo'q """

    queryset = CourseCategory.objects.filter(status=True)
    serializer_class = CourseCategory_APISerializer
    permission_classes = [AllowAny]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        queryset = CourseCategory.objects.filter(status=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CourseCategory_APISerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CourseCategory_APISerializer(queryset, many=True)
        return Response(serializer.data)
    
    """ HTTP_405_METHOD_NOT_ALLOWED """
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Course_Viewset(ModelViewSet):
    """ Kurs haqidama'lumot berish  uchun viewset
    faqat retrieve(GET) ishlaydi, qolgan metodlarga ruhsat yo'q """

    queryset  = Course.objects.filter(status=True)
    serializer_class = Course_APISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        queryset = Course.objects.filter(status=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = Courses_for_Category_APISerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = Courses_for_Category_APISerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = Course_APISerializer(instance)
        return Response(serializer.data)

    """ HTTP_405_METHOD_NOT_ALLOWED """
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Unit_Viewset(ModelViewSet):
    """ Darsga kirilganda chap tomonda bo'limlar va ulardagi mavzularning nomi ko'rinib turishi
     uchun viewset """
    queryset = Unit.objects.filter(status=True)
    serializer_class = Unit_APISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        queryset = Unit.objects.filter(status=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = Unit_APISerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = Unit_APISerializer(queryset, many=True)
        return Response(serializer.data)
    
    """ HTTP_405_METHOD_NOT_ALLOWED """
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Lesson_Viewset(ModelViewSet):
    """ Darslar uchun viewset """
    queryset  = Lessons.objects.filter(status=True)
    serializer_class = Lesson_APISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = Lesson_APISerializer(instance)
        return Response(serializer.data)

    """ HTTP_405_METHOD_NOT_ALLOWED """
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    
    
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Teacher_Viewset(ModelViewSet):
    """ O'qtuvchi uchun ma'lumot berish uchun viewset """

    queryset  = Teacher.objects.filter(status=True)
    serializer_class = Teacher_APISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        queryset = Teacher.objects.filter(status=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = Teachers_list_APISerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = Teachers_list_APISerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = Teacher_APISerializer(instance)
        return Response(serializer.data)

    """ HTTP_405_METHOD_NOT_ALLOWED """
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MyCourseViewSet(ModelViewSet):
    """ O'quvchi biror kursni 'MyCourse' bo'limiga qo'shishi uchun Viewset """
    queryset = MyCourse.objects.filter(status=True)
    serializer_class = MyCourse_APISerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        request_data = request.data

        try:
            student = Student.objects.get(id=request.user.id)
        except Exception as e:
            return Response({'error':"Bunday o'quvchi topilmadi"})

        try:
            if 'course' not in request_data:
                return Response({'error':"Bunday kurs topilmadi"})
            if old_course := MyCourse.objects.filter(student=student.id, course=request_data['course']):
                return Response({"error":"Siz avval bu kursni olgansiz ! Iltimos boshqa kurs tanlang !"})
            else:
                course = Course.objects.get(id=request_data['course'])
        except Exception as e:
            return Response({'error':"Kursning ma'lumotlarini saqlashda xatolik yuzaga keldi"})
        
        """--------------------------------------------"""

        # try:
        #     lessons = Lessons.objects.filter(unit= course.id) # lessons - O'quvchining tanlagan kursidagi darslar ro'yhati
        #     count = 1 # count - darslar ro'yhatidagi birinchi darni qirqib olish uchun miqdor 
        #     next_lesson = lessons[:count][0].id # next_lesson - birinchi darsning id si
        # except Exception as e:
        #     return Response({'error': "Bu Kursda darslar mavjud emas!"})


        """--------------------------------------------"""
        new_my_course = MyCourse.objects.create(
            student = student,
            course = course,
            next_lesson = None,
            # next_lesson = next_lesson,
        )
        new_my_course.save()
        # serializer = MyCourse_APISerializer(new_my_course) # eski holat
        message = f"Tabriklaymiz, Siz '{course.name}' kursiga muvaffaqiyatli a'zo bo'ldingiz !"
        return Response({'message': message})

    def list(self, request, *args, **kwargs):
        queryset = MyCourse.objects.filter(status=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = MyCourse_GET_APISerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MyCourse_GET_APISerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MyCourse_GET_APISerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        my_course = self.get_object()
        course_name = my_course.course.name
        my_course.delete()
        message = f"'{course_name}' kursi 'Mening kurslarim' qatoridan muvaffaqiyatli o'chirildi !"
        return Response({'message':message}, status=status.HTTP_204_NO_CONTENT)

    """ HTTP_405_METHOD_NOT_ALLOWED """
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)







