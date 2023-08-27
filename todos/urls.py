from django.urls import path

from . import views

app_name = "todos_api"
urlpatterns = [
    path("<int:pk>/", views.DetailTodoApi.as_view(), name="todo_detail"),
    path("", views.ListTodoApi.as_view(), name="todo_list"),
]
