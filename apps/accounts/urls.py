from django.urls import path
from apps.accounts import views


urlpatterns = [
    # --- Templates --- #
    path('login/', views.Login.as_view(), name='Login'),
    path('logout', views.Logout.as_view(), name='Logout'),
]
