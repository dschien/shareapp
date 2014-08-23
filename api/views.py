import json

from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api.models import Item, Transaction


@api_view(['POST'])
# @authentication_classes((OAuth2Authentication,))
@permission_classes((AllowAny,))
def requestItem(request, ):
    item_id = request.DATA['id']
    consumer_id = request.DATA['c_id']

    item = Item.objects.get_object_or_404(id=item_id)
    consumer = User.objects.get_object_or_404(id=consumer_id)

    t = Transaction(item=item, consumer=consumer)
    t.save()

    return HttpResponse(json.dumps(1))