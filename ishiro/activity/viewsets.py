from rest_framework import (viewsets, status)
from rest_framework.response import Response
from ishiro.activity.models import Activity
from ishiro.activity.serializers import ActivitySerializer
from ishiro.wallet.models import Wallet
from ishiro.account.saver.models import Saver


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    http_method_names = ['get', 'post', ]

    def get_serializer_context(self):
        context = {
            "request": self.request,
            "activity_type": self.kwargs.get('activity_type')
        }
        return context

    def get_queryset(self):
        user = self.request.user
        activity_type = self.kwargs['activity_type']
        queryset = Activity.objects.filter(activity_type=activity_type, wallet__owner=user)
        return queryset

