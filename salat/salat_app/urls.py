from django.urls import path, include
from .views import BasicInfoView, CSVFileView

urlpatterns = [
    path('view/', BasicInfoView.as_view()),
    path('load/', CSVFileView.as_view()),
]
