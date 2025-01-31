from django.urls import path, include

from TodoList import settings
from todo.views import (
    home_page,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_undo,
    task_complete,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path('', home_page, name="home-page"),
    path('task/create/', TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/undo/", task_undo, name="task-undo"),
    path("task/<int:pk>/complete/", task_complete, name="task-complete"),
    path("tag/list/", TagListView.as_view(), name="tag-list"),
    path('tag/create/', TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("", include(debug_toolbar.urls))] + urlpatterns

app_name = "todo"