
from django.urls import path,include
from . import views


urlpatterns=[
    path('codenights/',views.CreateListCodenightAPIView.as_view(),name='Codenight-listesi'),
]