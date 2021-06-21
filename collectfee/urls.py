
from django.urls import path
from . views import *
urlpatterns = [
    path('test-payment/', test_payment),
    path('save-stripe-info/', save_stripe_info),
    path('pay/', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success"),
    path('', home, name="home")
]
