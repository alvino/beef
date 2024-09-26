from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def homeView(request):
    return render(request, template_name='menu.html')
