from django.urls import path

from .views import profile_views, guest_views

app_name = "accounts"

urlpatterns = [
    ##Guest
    path('guest/', guest_views.Guest, name="guest"),

    ##Profile
    path('profile/new', profile_views.Profile_new, name="new_profile"),
    path('profile/<int:user_id>', profile_views.Profile_detail, name="profile"),
    path('profile/modify/<int:user_id>', profile_views.Profile_modify, name="profile_modify"),

    path('<int:user_id>/follow/', profile_views.Follow, name="follow"),#follow

    path('profile/delete/<int:user_id>', profile_views.User_delete, name="user_delete"), #delete/deactivate
]
