# urls.py
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', Registration.as_view(), name='registration' ),
    path('logout/', Logout.as_view(), name='logout'),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('qualitychecks/', QualityCheckListCreateView.as_view(), name='quality-check-list-create'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:pk>/checkout/', VehicleCheckoutView.as_view(), name='vehicle-checkout'),
]
