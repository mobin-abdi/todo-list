from django.shortcuts import render, redirect
from .models import TodoItem
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        context = request.POST.get('context', '')
        periority = request.POST.get('periority', 'M')
        TodoItem.objects.create(name=name, context=context, periority=periority)
        return redirect('home')
    
    todos = TodoItem.objects.all()
    return render(request, 'home.html', {"todos": todos})  

def delete_todo(request, id):
    try:
        todo = TodoItem.objects.get(id=id)
        todo.delete()
    except TodoItem.DoesNotExist:
        pass
    return redirect('home')