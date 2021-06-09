from roomChatBackend import views
from django.urls import path, include

urlpatterns=[
    path('signUp',views.SignUp.as_view())
]