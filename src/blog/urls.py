from django.urls import path
from .views import post_list, post_create, post_delete, post_update

app_name = "blog"
urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create"),
    path("<int:id>/delete/", post_delete, name="delete"),
    path("<int:id>/update/", post_update, name="update"),
]