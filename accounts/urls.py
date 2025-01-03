from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    ## SignUp
    path('signup/', views.Signup, name="signup"),

]