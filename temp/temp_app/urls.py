from django.urls import path
from temp_app.views import TodoView

urlpatterns = [
    path('todo', TodoView.as_view())
]
