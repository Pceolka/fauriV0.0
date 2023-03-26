from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import News
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse


# Создание видов


def news(request):
    newss = News.objects.order_by('-date')
    params = {}
    params["newss"] = newss
    return render(request, "news.html", params)


def single(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'single.html', {'news': news})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
