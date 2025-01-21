from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    #Profile
    path('profile/new', views.Profile_new, name="new_profile"),
    path('profile/<int:user_id>', views.Profile_detail, name="profile"),
    path('profile/modify/<int:user_id>', views.Profile_modify, name="profile_modify"),

    #follow
    path('<int:user_id>/follow/', views.Follow, name="follow"),
]
