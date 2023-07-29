from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseCategory_Viewset, Course_Viewset, Unit_Viewset, Lesson_Viewset, Teacher_Viewset,\
                    MyCourseViewSet 

app_name = 'course'
router = DefaultRouter()

""" --------------------------- COURSE APP --------------------------- """
router.register(r'category', CourseCategory_Viewset, 'category')
router.register(r'course', Course_Viewset, 'course')
router.register(r'unit', Unit_Viewset, 'unit')
router.register(r'lesson', Lesson_Viewset, 'lesson')
router.register(r'teacher', Teacher_Viewset, 'teacher')
router.register(r'my-course', MyCourseViewSet, 'my_course')


urlpatterns = [ 
    path('', include(router.urls))
]

