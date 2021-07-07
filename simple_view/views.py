from django.http import HttpResponse,JsonResponse
from simple_view.models import Message1
from django.core import serializers
impofrom django.http import HttpResponse,JsonResponse
from simple_view.models import Message1
from django.core import serializers
import json
from .models import Message1
from django.views.generic import View
# def create_view(request):
#     if request.method == "POST":

def create_view(request):
    # if request.method == "POST":
        post_response = (json.loads(request.body))
        message_obj = Message1.objects.create(message=post_response['message'],
                                             sender=post_response['sender'],
                                             receiver=post_response['receiver'],
                                             description=post_response['description'])

        status_response = {'status': True, 'code': 200}
        return HttpResponse(json.dumps(status_response))

