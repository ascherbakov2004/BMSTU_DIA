from django.urls import path
from .views import passport_list, passport_detail, create_application, add_to_cart, cart_view, remove_from_cart, applications_list, confirm_crossing, cancel_application

urlpatterns = [
    path('', passport_list, name='passport_list'),
    path('passport/<int:pk>/', passport_detail, name='passport_detail'),
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/<int:passport_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:passport_id>/', remove_from_cart, name='remove_from_cart'),
    path('create-application/', create_application, name='create_application'),
    path('applications/', applications_list, name='applications_list'),
    path("applications/confirm/<int:application_id>/", confirm_crossing, name="confirm_crossing"),
    path("applications/cancel/<int:application_id>/", cancel_application, name="cancel_application"),
]


