from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from user_management.models import Address, Customer, ProfileUser, Vendor
from user_management.serializers import AddressSerializer, CustomerSerializer, ProfileUserSerializer, VendorSerializer, UserSerializer

class AddressViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

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
    

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

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


class ProfileUserViewSet(viewsets.ModelViewSet):

        queryset = ProfileUser.objects.all()
        serializer_class = ProfileUserSerializer

        # @action(detail=False, methods=['get'])
        def list(self, request):
            # Functionality for listing all objects
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        # @action(detail=False, methods=['post'])
        def create(self, request):
            try:
                # Functionality for creating a new object
                address_data = request.data.get('address', {})
                user_data = request.data.get('user', {})
                profile_user_data = request.data.get('profile_user', {})
                
                # Serialize 'address' data
                address_serializer = AddressSerializer(data=address_data)
                address_serializer.is_valid(raise_exception=True)

                # Hash the user password before saving
                user_data['password'] = make_password(user_data.get('password'))

                # Serialize 'user' data
                user_serializer = UserSerializer(data=user_data)
                user_serializer.is_valid(raise_exception=True)

                # Serialize 'profile_user' data
                profile_user_serializer = ProfileUserSerializer(data=profile_user_data)

                # Save 'address', 'user' and 'profile_user'
                address = address_serializer.save()
                user = user_serializer.save()
                profile_user_data['user'] = user.id  # Link profile_user to the created user
                profile_user_data['addresses'] = [address.id]
                profile_user_serializer.is_valid(raise_exception=True)
                profile_user_serializer.save()

                # Return response
                headers = self.get_success_headers(user_serializer.data)
                return Response(user_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            except:
                # Handle exceptions (customize this section based on your needs)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
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


class VendorViewSet(viewsets.ModelViewSet):

        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer

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