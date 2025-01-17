from django.urls import path

from .views import base_views
from .views import post_views
from .views import comment_views

app_name = "diary"

urlpatterns = [
    ### MAIN CONTENT

    path('', base_views.Index, name="index"),
    path('detail/<int:diary_id>',base_views.Detail, name="detail"),

    ##CRUD
    #create
    path('new/', post_views.New, name="new"),
    path('create/', post_views.Create, name="create"),

    #update
    path('edit/',post_views.Edit, name="edit"),
    path('update/<int:diary_id>/',post_views.Update, name="update"),

    #delete
    path('delete/<int:diary_id>/', post_views.Delete, name="delete"),


    ### COMMENT

    #create
    path('<int:diary_id>/comment', comment_views.Create_comment, name="comment_create"),
    path('<int:diary_id>/comment/<int:parent_id>', comment_views.Create_comment, name='comment_reply'), #reply-comment

    #update
    path('<int:diary_id>/comment/<int:comment_id>/update', comment_views.Update_comment, name="comment_update"),
     # reply-comment

    path('<int:diary_id>/comment/<int:comment_id>/delete', comment_views.Delete_comment, name="comment_delete"),

    
    
]