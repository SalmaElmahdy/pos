from rest_framework import viewsets

from .permisssions import IsCashierOrSupervisor
from rest_framework.permissions import IsAuthenticated

from .models import order
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCashierOrSupervisor]
    
    @action(detail=True, methods=['get'], url_path='string-representation')
    def string_representation(self, request, pk=None):
        order = self.get_object()  
        return Response({"string_representation": str(order)})  