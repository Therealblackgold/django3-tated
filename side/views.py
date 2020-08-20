from django.shortcuts import render
from .models import Side


def home(request):
    sides = Side.objects.order_by('-date')
    return render(request, 'side/home.html', {'sides': sides})


