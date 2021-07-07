from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
from app1.serializers import MessageSerializer
from django.views.generic import RedirectView
from django.http.response import JsonResponse
from app1.db_insert import sql_conn

@api_view(['POST'])
def message_save_view(request):
    post_response = (json.loads(request.body))
    # message = post_response["message"]
    # sender = post_response["sender"]
    # receiver = post_response["receiver"]
    # description = post_response["description"]
    # obj = sql_conn()
    # print(type(post_response))
    # obj.fndbinsert(message,sender,receiver,description)
    # """insert data with serializer"""

    serializer = MessageSerializer(data = post_response)      # change serializer  var nname
    if serializer.is_valid():
        serializer.save()
        # return JsonResponse(serializer.data,status=200)
    return HttpResponse("message created successfully")
