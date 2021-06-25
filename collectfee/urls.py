
from django.urls import path
from . views import *
# from . fb_admin import fireTest
urlpatterns = [
    path('applications/', applications, name='applications'),
    path('applications/<str:pk>/', singleApplication, name='singleapplication' ),
    path('test-payment/', test_payment),
    path('save-stripe-info/', save_stripe_info),
    path('pay/', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success"),
    path('', home, name="home"),
    # path('firetest/', fireTest, name="firetest"),
    path('api/application/', api_create_application),
    path('api/applicationlist/', viewApplications),
    path('sendmail/<str:pk>/', sendmail, name="sendmail"),
    
    
]
