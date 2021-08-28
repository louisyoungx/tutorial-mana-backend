from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Django_Admin import settings
from django.urls import include, path

from rest_framework import routers
from Applications.Global import views as GlobalView
from Applications.Teacher import views as TeacherView
from Applications.Student import views as StudentView

router = routers.DefaultRouter()
router.register(r'users', GlobalView.UserViewSet)
router.register(r'groups', GlobalView.GroupViewSet)
router.register(r'Teacher', TeacherView.TeacherViewSet)
router.register(r'Course', TeacherView.CourseViewSet)
router.register(r'Tutorial', TeacherView.TutorialViewSet)
router.register(r'student', StudentView.StudentViewSet)
router.register(r'join-course', StudentView.JoinedCourseViewSet)
router.register(r'join-tutorial', StudentView.JoinedTutorialViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('/teacher', include("Applications.Teacher.urls")),
    # path('/student', include("Applications.Student.urls")),
]   + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
