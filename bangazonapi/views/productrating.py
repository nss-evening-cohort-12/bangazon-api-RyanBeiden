from django.core.exceptions import ValidationError
from django.http.response import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from bangazonapi.models import ProductRating, Customer, Product

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ('id', 'customer', 'product', 'rating')


class ProductRatings(ViewSet):

    def list(self, request):
        ratings = ProductRating.objects.all()

        serializer = ProductRatingSerializer(
            ratings, many=True, context={'request': request}
        )

        return Response(serializer.data)

    def create(self, request):

        product = Product.objects.get(pk=request.data['product'])

        productrating = ProductRating()
        productrating.rating = request.data['rating']
        productrating.customer = Customer.objects.get(user=request.auth.user)
        productrating.product = product

        try:
            productrating.save()
            serializer = ProductRatingSerializer(productrating, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
