from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.http import Http404
from purchase_management.models import Purchase, PurchaseProduct, Inventory
from purchase_management.serializers import PurchaseSerializer, PurchaseProductSerializer, InventorySerializer
from user_management.serializers import AddressSerializer, VendorSerializer

class PurchaseViewSet(viewsets.ModelViewSet):

    queryset = Purchase.objects.filter(deleted=False)
    serializer_class = PurchaseSerializer

    def list(self, request):    
        try:
            # Functionality for listing all objects
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            # Handle the exception and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            return Response(request.data.get('purchase_products, []'))
            # vendor_address_data = {
            #     'address_line_1': request.data.get('vendor_address[address_line_1]', ''),
            #     'address_line_2': request.data.get('vendor_address[address_line_2]', ''),
            #     'city': request.data.get('vendor_address[city]', ''),
            #     'district': request.data.get('vendor_address[district]', ''),
            #     'state': request.data.get('vendor_address[state]', ''),
            #     'country': request.data.get('vendor_address[country]', ''),
            #     'postal_code': request.data.get('vendor_address[postal_code]', ''),
            #     'created_by': request.data.get('vendor_address[created_by]', ''),
            #     'updated_by': request.data.get('vendor_address[updated_by]', ''),
            # }
            # address_serializer = AddressSerializer(data=vendor_address_data)
            # address_serializer.is_valid(raise_exception=True)
            # vendor_address = address_serializer.save()

            # vendor_data = {
            #     'name': request.data.get('vendor[name]', ''),
            #     'gst_no': request.data.get('vendor[gst_no]', ''),
            #     'email_id': request.data.get('vendor[email_id]', ''),
            #     'phone_no': request.data.get('vendor[phone_no]', ''),
            #     'created_by': request.data.get('vendor[created_by]', ''),
            #     'updated_by': request.data.get('vendor[updated_by]', ''),
            # }
            # vendor_data['address'] = vendor_address['id']
            # vendor_serializer = VendorSerializer(data=vendor_data)
            # vendor_serializer.is_valid(raise_exception=True)
            # vendor = vendor_serializer.save()

            # purchase_data = {
            #     'invoice_no': request.data.get('purchase[invoice_no]', ''),
            #     'invoice_date': request.data.get('purchase[invoice_date]', ''),
            #     'purchase_order_no': request.data.get('purchase[purchase_order_no]', ''),
            #     'place_of_supply': request.data.get('purchase[place_of_supply]', ''),
            #     'created_by': request.data.get('purchase[created_by]', ''),
            #     'updated_by': request.data.get('purchase[updated_by]', ''),
            # }
            # purchase_data['vendor'] = vendor['id']
            # purchase_serializer = PurchaseSerializer(data=purchase_data)
            # purchase_serializer.is_valid(raise_exception=True)
            # purchase = purchase_serializer.save()



            
            return Response(address_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Handle the exception and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            # Functionality for retrieving a single object by ID
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            # Functionality for updating a single object by ID
            instance = self.get_object()
            images_data = request.data.getlist('images', [])
            request.data.pop('images', None)
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Handle images update
            instance.images.clear()  # Clear existing images
            for image_data in images_data:
                instance.images.create(image=image_data)

            return Response(serializer.data)

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except serializers.ValidationError as e:
            # Handle the case when the serializer validation fails
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, *args, **kwargs):    
        try:
            instance = self.get_object()
            instance.soft_delete()  # Call the soft_delete method from your model
            return Response({'message': 'Product successfully deleted.', 'status': 200})

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

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