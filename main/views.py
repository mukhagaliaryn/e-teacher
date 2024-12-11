from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Main view
def main(request):
    return render(request, 'index.html', {})


# Home view
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home/index.html', {})