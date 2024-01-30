from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from apps.store.models import Product
from apps.store.serializers import ProductSerializer
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


class HomeTemplate(APIView):

    def get(self, request):
        return render(request, 'pages/store/home.html', {'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})
    

class ProductTemplate(APIView):

    def get(self, request, slug):
        return render(request, 'pages/store/product.html')


class ProductListCreateView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        limit = request.query_params.get('limit')
        if limit:
            products = Product.objects.order_by('id')[:int(limit)]
        else:
            products = Product.objects.order_by('id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductRetrieveUpdateDestroyView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCheckoutSession(APIView):
    
    def post(self, request):
        line_items = []
        products = sorted(request.data['products'], key=lambda x: x['id'])
        products_id = [product['id'] for product in products]
        products_volume = [product['volume'] for product in products]
        products = Product.objects.filter(id__in=products_id)
        for index, product in enumerate(products):
            line_items.append(
                {
                    'price_data': {
                        'currency': 'BRL',
                        'unit_amount': int(product.price),
                        'product_data': {
                            'name': product.name
                        }
                    },
                    'quantity': products_volume[index],
                },
            )

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            payment_method_types=[
                'card',
                'boleto',
            ],
            metadata={
                'id_product': 1,
            },
            mode='payment',
            success_url=f'{request.scheme}://{request.get_host()}{reverse("HomeTemplate")}',
            cancel_url=f'{request.scheme}://{request.get_host()}{reverse("HomeTemplate")}',
        )

        return JsonResponse({'id': checkout_session.id})
