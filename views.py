from django.shortcuts import render
from django.http import HttpResponse
from Quiz.models import Quiz


# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")

# Create your views here.
def quiz_view(request):
    quiz=Quiz.objects.all()
    return render(request,'index.html',{'quiz':quiz})

