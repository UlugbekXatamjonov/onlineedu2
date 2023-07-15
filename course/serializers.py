from rest_framework import serializers

from .models import Teacher, Course, Unit, Lessons, File, MyCourse, CourseCategory


"""
TO DO:
CoursCategory section ✔
Course section ✔
Unit section ✔
Lessons section ✔
Teacher section ✔

"""

""" ------------------------------------------------------------------------------   
                                Free Courses Section 
---------------------------------------------------------------------------------- """

""" CoursCategory section Serializers """
class Courses_for_Category_APISerializer(serializers.ModelSerializer):
    """ Kurslarning Categoriya bo'limi uchun Kursning ma'lumotlari """

    teacher_name = serializers.CharField(source='teacher.full_name')
    teacher_slug = serializers.CharField(source='teacher.slug')

    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'cost', 'photo', \
                    'teacher', 'teacher_name', 'teacher_slug',\
                    )
        
class CourseCategory_APISerializer(serializers.ModelSerializer):
    """ Kurslarning kategoriya bo'limi ma'lumotlari """

    courses = Courses_for_Category_APISerializer(many=True,read_only=True)
    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'slug', \
                    'courses'
                    )


""" Course section Serializers """
class Lessons_for_Course_APISerializer(serializers.ModelSerializer):
    """ Kurs bo'limi uchun o'sha kursdagi dasrlar haqida ma'lumot berish uchun serializer """

    class Meta:
        model = Lessons
        fields = ('id', 'name', 'slug')

class Units_for_Course_APISerializer(serializers.ModelSerializer):
    """ Kurs bo'limi uchun o'sha kursdagi unitlar(bo'limlar) haqida ma'lumot berish uchun serializer """

    lessons = Lessons_for_Course_APISerializer(many=True, read_only=True)
    class Meta:
        model = Unit
        fields = ('id', 'name', 'slug', \
                    'lessons'
                    )

class Course_APISerializer(serializers.ModelSerializer):
    """ Kurs bo'limi uchun o'sha kurs haqida ma'lumot berish uchun serializer """

    units = Units_for_Course_APISerializer(many=True, read_only=True)
    teacher_name = serializers.CharField(source='teacher.full_name')
    teacher_slug = serializers.CharField(source='teacher.slug')
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')

    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'lesson_count', 'cost', 'about', 'photo', 'short_video',\
                    'teacher', 'teacher_name', 'teacher_slug', \
                    'category', 'category_name', 'category_slug', \
                    'units'
                    )
        
""" Unit section Serializers """
class Lessons_for_Unit_APISerializer(serializers.ModelSerializer):
    """ Bo'limlar va ulardagi mavzularning nomini chiqaradigan oyna uchun lesson(darslar) serializeri """
    class Meta:
        model = Lessons
        fields = ('id', 'name', 'slug')

class Unit_APISerializer(serializers.ModelSerializer):
    """ Bo'limlar va ulardagi mavzularning nomini chiqaradigan oyna uchun unit(bo'limlar) serializeri """
    lessons = Lessons_for_Unit_APISerializer(many=True, read_only=True)
    class Meta:
        model = Unit
        fields = ('id', 'name', 'slug', 'lessons')


""" Lessons section Serializers """
class File_APISerializer(serializers.ModelSerializer):
    """ Dats ichidagi file lar uchun serializer  """
    class Meta:
        model = File
        fields = ('file',)

class Lesson_APISerializer(serializers.ModelSerializer):
    """ Dars va undagi materiallar uchun serializer """
    files = File_APISerializer(many=True, read_only=True)
    unit_name = serializers.CharField(source='unit.name')
    unit_slug = serializers.CharField(source='unit.slug')
    # examp = ExampAPISerializer(many=True, read_only=True)
    
    class Meta:
        model = Lessons
        fields = ('id', 'name', 'slug', 'about', 'video', 'body', 
                    'unit', 'unit_name', 'unit_slug',
                    'files', 
                    # 'examp'
                  )


""" Teacher section Serializer """
class Courses_for_Teacher_APISerializer(serializers.ModelSerializer):
    """ Kurs bo'limi uchun o'sha kurs haqida ma'lumot berish uchun serializer """

    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')

    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'lesson_count', 'cost', 'photo', \
                    'category', 'category_name', 'category_slug', \
                    )

class Teacher_APISerializer(serializers.ModelSerializer):
    """ O'qtuvchilar haqida ma'lumot berish uchun serializer """

    courses = Courses_for_Teacher_APISerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'slug', 'age', 'degree', 'about', 'photo', \
                    'courses'
                    )

class Teachers_list_APISerializer(serializers.ModelSerializer):
    """ O'qtuvchilar haqida ma'lumot berish uchun serializer """
        
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'slug', 'age', 'degree', 'photo')


""" Account Section """
# class MyCourseAPISerializer(serializers.ModelSerializer):
#     course_name = serializers.CharField(source='course.name')
#     course_lesson_count = serializers.IntegerField(source='course.lesson_count')
#     course_slug = serializers.CharField(source='course.slug')
    
#     class Meta:
#         model = MyCourse
#         fields = ('id', 'student', 'slug', 'course', 'course_name', 'course_slug', 'course_lesson_count',\
#                    'coin', 'ball', 'next_lesson')


