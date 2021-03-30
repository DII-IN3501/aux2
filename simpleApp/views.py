from django.shortcuts import render

def index(request, nombre="tú"):
    return render(request, 'simpleApp/index.html', {'nombre':nombre})
