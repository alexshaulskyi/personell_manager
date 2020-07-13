from django.urls import path, include

from users.views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include("django.contrib.auth.urls")),
]