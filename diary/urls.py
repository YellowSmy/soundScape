from django.urls import path

from .views import base_views
from .views import post_views
from .views import comment_views
from .views import music_views

app_name = "diary"

urlpatterns = [
    ## BASIC CONTENT
    path('', base_views.Index, name="index"),
    path('detail/<int:diary_id>',base_views.Detail, name="detail"),
    path('like/<int:diary_id>', base_views.Like, name="like"), #like
    path('temp/', base_views.Temp_save, name="temp"),
    path('change-theme/', base_views.Change_theme, name="change_theme"),

    ## CRUD
    path('search', music_views.Search, name="search"), #search music 
    path('create/', post_views.Create, name="create"),

    path('update/<int:diary_id>/',post_views.Update, name="update"),
    path('delete/<int:diary_id>/', post_views.Delete, name="delete"),

    ### COMMENT
    path('<int:diary_id>/comment', comment_views.Create_comment, name="comment_create"),
    path('<int:diary_id>/comment/<int:parent_id>', comment_views.Create_comment, name='comment_reply'), #reply-comment
    path('<int:diary_id>/comment/<int:comment_id>/update', comment_views.Update_comment, name="comment_update"),
    path('<int:diary_id>/comment/<int:comment_id>/delete', comment_views.Delete_comment, name="comment_delete"),   
]