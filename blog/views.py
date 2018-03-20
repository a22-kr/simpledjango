from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    m = {'обезьяна','кенгуру','собака','ягуар'}
    return render(request, 'blog/index.html', {'animals': m})

