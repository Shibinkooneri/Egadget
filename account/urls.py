from django.urls import path
from .views import *

urlpatterns=[
    path('reg',SignUpView.as_view(),name='signup'),
    path('lout',Logout.as_view(),name='lout')
]