from django.urls import path

from Applications.Global.views import Token

app_name = 'student'

urlpatterns = [
    path('Token/', Token.as_view(), name='token'),
]
