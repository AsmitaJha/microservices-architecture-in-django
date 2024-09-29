from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action

PRODUCT_SERVICE_URL = "http://127.0.0.1:8000/products/"  # ***Internal API communication (this is the difference between monolithic and microservices. In microservices, we have to extract the product_id through the url of product api***)
"""instead of above url, we can put this for microservices
from products.models import Product

def create_order(request):
    product=Product.objects.get(id=product_id)  #direct database access"""


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["post"])
    def create_order(self, request):
        user = request.data.get("user")
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")

        # Fetch product details from Product service (API call)
        product_response = requests.get(f"{PRODUCT_SERVICE_URL}{product_id}/")

        if product_response.status_code != 200:
            return Response({"error": "Product not found"}, status=404)

        # Create order
        order = Order.objects.create(
            user_id=user, product_id=product_id, quantity=quantity
        )
        return Response(
            {
                "message": "Order placed successfully",
                "order": OrderSerializer(order).data,
                "product": product_response.json(),
            }
        )
