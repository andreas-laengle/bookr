from tkinter.font import names
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})
