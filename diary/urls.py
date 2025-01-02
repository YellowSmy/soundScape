from django.urls import path

from . import views

app_name = "diary"

urlpatterns = [
    ## Basic Page
    path('', views.Index, name="index"),
    path('detail/<int:diary_id>',views.Detail, name="detail"),

    ## CRUD
    #create
    path('new/', views.New, name="new"),
    path('create/', views.Create, name="create"),

    #update
    path('edit/',views.Edit, name="edit"),
    path('update/<int:diary_id>/',views.Update, name="update"),

    #delete
    path('delete/<int:diary_id>/', views.Delete, name="delete"),
]