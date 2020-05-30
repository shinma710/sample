"""This is a test program."""
from django.shortcuts import render
from .forms import UserForm


def index(request):
    context = {
        'name' : 'iima',
    }
    return render(request, 'sample_app/index.html', context)

def about(request):
    """/about アバウトページ"""
    return render(request, 'sample_app/about.html')

def info(request):
    """/info インフォページ"""
    return render(request, 'sample_app/info.html')

def question(request):
    params = {'name': '', 'email': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        params['name'] = request.POST['name']
        params['email'] = request.POST['email']
        params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'sample_app/question.html', params)
