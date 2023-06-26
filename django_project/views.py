from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def thanks(request):
    return render(request, "thanks.html")