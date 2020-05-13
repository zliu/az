from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import invTypes
import requests

# Create your views here.

def type_list(request):
    types = get_object_or_404(invTypes, pk=34)

    return render(request, 'eve/type_list.html', {'types': types})
