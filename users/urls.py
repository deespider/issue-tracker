from django.urls import path, include
from users.views import SignUpView, LoginView

urlpatterns = [
    # Other URL patterns...
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
]