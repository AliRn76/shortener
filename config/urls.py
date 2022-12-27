from django.urls import path
from app.views import CreateAPIView, RedirectAPIView

urlpatterns = [
    path('', CreateAPIView.as_view()),
    path('<slug:url>', RedirectAPIView.as_view()),
]
