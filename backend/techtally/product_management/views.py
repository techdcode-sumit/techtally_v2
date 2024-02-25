from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.http import Http404
from product_management.models import Brand, Category, SubCategory, Product, ProductImage
from product_management.serializers import BrandSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.filter(deleted=False)
    serializer_class = BrandSerializer

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
            # Functionality for creating a new object
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except serializer.ValidationError as e:
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
            return Response({'message': 'Brand successfully deleted.', 'status': 200})

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.filter(deleted=False)
    serializer_class = CategorySerializer

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
            # Functionality for creating a new object
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except serializer.ValidationError as e:
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
            return Response({'message': 'Category successfully deleted.', 'status': 200})

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubCategoryViewSet(viewsets.ModelViewSet):

    queryset = SubCategory.objects.filter(deleted=False)
    serializer_class = SubCategorySerializer

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
            # Functionality for creating a new object
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except serializer.ValidationError as e:
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
            return Response({'message': 'SubCategory successfully deleted.', 'status': 200})

        except Http404:
            # Handle the case when the object is not found
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions and provide an appropriate response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer

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
            # Functionality for creating a new object
            images = request.data.getlist('images', [])
            request.data.pop('images', None)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product_instance = serializer.save()

            for image in images:
                product_instance.images.create(image=image)

            # Serialize the final product instance with images
            final_serializer = self.get_serializer(product_instance)
            return Response(final_serializer.data, status=status.HTTP_201_CREATED)

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