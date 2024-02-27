from rest_framework import viewsets
from ishiro.budget.serializers import BudgetSerializer
from datetime import datetime

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        month = datetime.now().month
        queryset = model.objects.filter(owner=self.request.user, period__month__gte=month)
        return queryset
