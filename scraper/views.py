from django.shortcuts import render
from django.http import JsonResponse

def article_list(request):
    data = {
        'title0':'url0',
        'titl1':'url1'
    }
    return JsonResponse(data)
