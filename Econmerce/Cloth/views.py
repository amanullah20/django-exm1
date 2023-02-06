from django.shortcuts import render

# Create your views here.


def cloth(request):
    return render(request, 'cloth.html', {'course': 'Django'})
