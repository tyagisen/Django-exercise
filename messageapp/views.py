from messageapp.serializers import MsgSerializer
from rest_framework import viewsets
from .models import Msg
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle


class MsgModelViewSet(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]


