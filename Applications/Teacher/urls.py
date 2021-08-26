from django.urls import path

from Applications.Global.views import Token

app_name = 'teacher'

urlpatterns = [
    path('Token/', Token.as_view(), name='token'),
]
