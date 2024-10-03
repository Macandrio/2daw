from django.shortcuts import render
from .models import protectora

# Create your views here.
#def post_list(request) :
#    protectora = protectora.objects.all()
#    return render(request, 'Protectora/post_list.html', {'posts_mostrar': protectora})


def post_list(request) :
    Protectora = protectora.objects.all()
    return render(request, 'protectora/post_list.html', {'protectora_mostrar': Protectora})