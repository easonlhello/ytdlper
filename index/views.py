from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    return render(request, 'index.html')