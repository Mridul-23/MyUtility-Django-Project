from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def calc(request):
    return render(request, "calc.html")