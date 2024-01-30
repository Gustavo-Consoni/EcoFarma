from django.urls import path
from apps.store import views


urlpatterns = [
    # --- Templates --- #
    path('', views.HomeTemplate.as_view(), name='HomeTemplate'),
    path('produto/<str:slug>', views.ProductTemplate.as_view(), name='ProductTemplate'),
    
    # --- API --- #
    path('api/v1/products', views.ProductListCreateView.as_view()),
    path('api/v1/products/<int:id>', views.ProductRetrieveUpdateDestroyView.as_view()),
    path('api/v1/create_checkout_session', views.CreateCheckoutSession.as_view()),
]
