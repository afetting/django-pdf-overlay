from django.urls import path
from .views import PrintTestView

urlpatterns = [
    path('', PrintTestView.as_view(), name='print-test'),
]