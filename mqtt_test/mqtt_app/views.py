import json

from django.http import JsonResponse

from.mqtt import client as mqtt_client
from . models import *
print('views')
def publish_message(request):
    request_data = json.loads(request.body)
    print('request_data',request_data)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    print('rc',rc)
    print('mid',mid)
    

    return JsonResponse({'code': rc})



# import json
# from django.http import JsonResponse
# # from . import mqtt
# from mqtt_test.mqtt import client as mqtt_client
#
# def publish_message(request):
#     print(request.body)
#     try:
#         request_data = json.loads(request.body)
#
#         print('request_data', request_data)
#
#         if not request_data:
#             return JsonResponse({'error': 'Empty request body'}, status=400)
#         rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
#         return JsonResponse({'code': rc})
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON format'}, status=400)
