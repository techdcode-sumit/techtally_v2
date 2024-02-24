from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from purchase_management.models import Purchase, PurchaseProduct, Inventory
from purchase_management.serializers import PurchaseSerializer, PurchaseProductSerializer, InventorySerializer

class PurchaseViewSet(viewsets.ModelViewSet):

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    # @action(detail=False, methods=['get'])
    def list(self, request):
        # Functionality for listing all objects
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=['post'])
    def create(self, request):
        # Functionality for creating a new object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    # @action(detail=True, methods=['get'])
    def retrieve(self, request, pk=None):
        # Functionality for retrieving a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    
    # @action(detail=True, methods=['put'])
    def update(self, request, pk=None):
        # Functionality for updating a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # @action(detail=False, methods=['patch'])
    def partial_update(self, request, pk=None):
        # Functionality for partially updating a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class PurchaseProductViewSet(viewsets.ModelViewSet):

    queryset = PurchaseProduct.objects.all()
    serializer_class = PurchaseProductSerializer

    # @action(detail=False, methods=['get'])
    def list(self, request):
        # Functionality for listing all objects
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=['post'])
    def create(self, request):
        # Functionality for creating a new object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    # @action(detail=True, methods=['get'])
    def retrieve(self, request, pk=None):
        # Functionality for retrieving a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    
    # @action(detail=True, methods=['put'])
    def update(self, request, pk=None):
        # Functionality for updating a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # @action(detail=False, methods=['patch'])
    def partial_update(self, request, pk=None):
        # Functionality for partially updating a single object by ID
        queryset = self.get_queryset()
        obj = self.get_object(queryset, pk=pk)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class InventoryViewSet(viewsets.ModelViewSet):

        queryset = Inventory.objects.all()
        serializer_class = InventorySerializer

        # @action(detail=False, methods=['get'])
        def list(self, request):
            # Functionality for listing all objects
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        # @action(detail=False, methods=['post'])
        def create(self, request):
            # Functionality for creating a new object
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
        
        # @action(detail=True, methods=['get'])
        def retrieve(self, request, pk=None):
            # Functionality for retrieving a single object by ID
            queryset = self.get_queryset()
            obj = self.get_object(queryset, pk=pk)
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        
        # @action(detail=True, methods=['put'])
        def update(self, request, pk=None):
            # Functionality for updating a single object by ID
            queryset = self.get_queryset()
            obj = self.get_object(queryset, pk=pk)
            serializer = self.get_serializer(obj, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        # @action(detail=False, methods=['patch'])
        def partial_update(self, request, pk=None):
            # Functionality for partially updating a single object by ID
            queryset = self.get_queryset()
            obj = self.get_object(queryset, pk=pk)
            serializer = self.get_serializer(obj, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)