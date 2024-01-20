from django.shortcuts import render

def home(request):
    return render(request, "a_plot/index.html")


