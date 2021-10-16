from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def client(request):
    
    if request.method == 'GET':
        return JsonResponse(list(find_all()), safe=False, content_type="application/json",
            json_dumps_params={'ensure_ascii': False})

    return ''

def find_all():

    client_one = {
                    "id": 1,
                    "name": "JUAN PEREZ CASTRO",                    
                }

    client_two = {
                    "id": 2,
                    "name": "PEDRO TAPIA HERRERA",                    
                }
    return [client_one, client_two]


