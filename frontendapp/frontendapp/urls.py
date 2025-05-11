# myapp/urls.py

from django.urls import path
from upload.views import deepfake_detector

urlpatterns = [
    path("detect/", deepfake_detector, name="deepfake_detector"),
]
