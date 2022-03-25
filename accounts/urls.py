from django.urls import path
from accounts import views

app_name="accounts"

urlpatterns=[

    path('signin/',views.SignupView,name='signup'),
    path('login/',views.LoginView,name="login"),
    path("logout/",views.LogOutView,name="logout")
]