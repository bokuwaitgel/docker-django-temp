from rest_framework.response import Response
from rest_framework.views import APIView

from temp_app.models import Todo

class TodoView(APIView):
    
    def post (self, request):
        task = request.data.get('task')
        completed = request.data.get('completed')
        todo = Todo.objects.create(task=task, completed=completed)
        return Response(200)
    
    def get(self, request):
        todos = Todo.objects.all()
        return Response([{'task': todo.task, 'completed': todo.completed} for todo in todos])
    
    #delete method
    def delete(self, request):
        task = request.data.get('task')
        Todo.objects.filter(task=task).delete()
        return Response(200)