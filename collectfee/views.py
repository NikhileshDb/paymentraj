from django.shortcuts import render
import stripe
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from . models import *

stripe.api_key = 'sk_test_51B8dmzKYbyr1xLhvvWluiihZYPwNoQuzQbUMEaywd91dQ0q1hFJ7SdYHc2uxEis3i8nIZPeutsBzjqqHyRNLTDR8009F1BbuPH'


@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
    amount=1000, currency='pln', 
    payment_method_types=['card'],
    receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)
@api_view(['POST'])
def save_stripe_info(request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    extra_msg = '' # add new variable to response message

    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data

    # if the array is empty it means the email has not been used yet  
    if len(customer_data) == 0:
        # creating customer
        customer = stripe.Customer.create(
        email=email, payment_method=payment_method_id)
    
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."
    
    stripe.PaymentIntent.create(
    customer=customer, 
    payment_method=payment_method_id,  
    currency='pln', # you can provide any currency you want
    amount=1500, # I modified amount to distinguish payments
    confirm=True)
    
    return Response(status=status.HTTP_200_OK,
        data = {
            'message': 'Success',
            'data': {'customer_id': customer.id,
            'extra_msg': extra_msg},
        })

###########################################################################################################################
#RazorPay Start
###########################################################################################################################
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Order
from .serailizers import OrderSerializer, ApplicationSerializer
import json

import environ
import razorpay

env= environ.Env()

# you have to create .env file in same folder where you are using environ.Env()
# reading .env file which located in api folder
environ.Env.read_env()

@api_view(['POST'])
def start_payment(request):
    #request.data is coming from frontend
    amount = request.data['amount']
    name = request.data['name']

    # setup razorpay client this is the client to whome user is paying money that's you
    client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
    # mumtiply it by 100 so it will be 50 rupees.
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next 
    # function
    order = Order.objects.create(order_product=name, 
                                 order_amount=amount, 
                                 order_payment_id=payment['id'])
    
    serializer = OrderSerializer(order)

    data = {
        "payment": payment,
        "order": serializer.data
    }

    return Response(data)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from the frontend

    res = json.loads(request.data["response"])
    print(res)
    """res will be:
    {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
    'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    this will come from frontend which we will use to validate and confirm the payment
    """

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""
    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    order = Order.objects.get(order_payment_id=ord_id)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

    # razorpay client if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)




def home(request):
    payments = Order.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'index.html', context)


# from firebase import firebase

# firebase = firebase.FirebaseApplication('https://rajarshi-8c7cc-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
# data = {'Name': 'Vivek',
#         'RollNo': 1,
#         'Percentage': 76.02}
# # result = firebase.post('user/', data)

# # print(result)


@api_view(['POST'])
def api_create_application(request):
    if request.method != 'POST':
        comment = {'invalid': 'Invalid Methode'}
        return Response(comment, status=status.HTTP_400_BAD_REQUEST)
    else:
        FirstName = request.data.get['firstName']
        MiddleName = request.data.get['middleName']
        LastName = request.data.get['lastName']
        Aadhaar = request.data.get['aadhaar']
        Martial = request.data.get['martial']
        Mobile = request.data.get['mobile']
        Email = request.data.get['email']
        MotherName = request.data.get['motherName']
        FatherName = request.data.get['fatherName']
        AnnualIncome = request.data.get['annualIncome']
        AnyOtherUni = request.data.get['anyotheruni']

        #Addresses
        Address = request.data.get['address']
        Pincode = request.data.get['pincode ']
        Category = request.data.get['category']
        Minority = request.data.get['minority']
        State = request.data.get['state']
        City = request.data.get['city']
        DateOfBirth = request.data.get['dob']
        Nationality = request.data.get['nationality']

        #Extra Details
        PayingGuest = request.data.get['payingguest']
        Transport = request.data.get['transport']

        #Sunjects
        Elective1 = request.data.get['elective1']
        Elective2 = request.data.get['elective2']
        Elective3 = request.data.get['elective3']

        Preference1 = request.data.get['preference1']
        Preference2 = request.data.get['preference2']
        Preference3 = request.data.get['preference3']

        Employment = request.data.get['employment']

        FullMarks1 = request.data.get['fullmarks1']
        FullMarks2 = request.data.get['fullmarks2']
        FullMarks3 = request.data.get['fullmarks3']
        FullMarks4 = request.data.get['fullmarks4']
        FullMarks5 = request.data.get['fullmarks5']
        FullMarks6 = request.data.get['fullmarks6']

        MarkObtain1 = request.data.get['markObtain1']
        MarkObtain2 = request.data.get['markObtain2']
        MarkObtain3 = request.data.get['markObtain3']
        MarkObtain4 = request.data.get['markObtain4']
        MarkObtain5 = request.data.get['markObtain5']
        MarkObtain6 = request.data.get['markObtain6']

        Grade1 = request.data.get['grade1']
        Grade2 = request.data.get['grade2']
        Grade3 = request.data.get['grade3']
        Grade4 = request.data.get['grade4']
        Grade5 = request.data.get['grade5']
        Grade6 = request.data.get['grade6']

        Percentage = request.data.get['percentage']

        try:
            application = ApplicationSerializer(
                FirstName = FirstName,
                MiddleName = MiddleName,
                LastName = LastName,
                Aadhaar = Aadhaar,
                Martial = Martial,
                Mobile = Mobile,
                Email = Email,
                MotherName = MotherName,
                FatherName = FatherName,
                AnnualIncome = AnnualIncome,
                AnyOtherUni = AnyOtherUni,
                #Address
                Address = Address,
                Pincode = Pincode,
                Category = Category,
                Minority = Minority,
                State = State,
                City = City,
                DateOfBirth = DateOfBirth,
                Nationality = Nationality,
                #ExtraDetails
                Elective1 = Elective1,
                Elective2 = Elective2,
                Elective3 = Elective3,
                Preference1 = Preference1,
                Preference2 = Preference2,
                Preference3 = Preference3,

                Employment = Employment,
                FullMarks1 = FullMarks1,
                FullMarks2 = FullMarks2,
                FullMarks3 = FullMarks3,
                FullMarks4 = FullMarks4,
                FullMarks5 = FullMarks5,
                FullMarks6 = FullMarks6,

                MarkObtain1 = MarkObtain1,
                MarkObtain2 = MarkObtain2,
                MarkObtain3 = MarkObtain3,
                MarkObtain4 = MarkObtain4,
                MarkObtain5 = MarkObtain5,
                MarkObtain6 = MarkObtain6,

                Grade1 = Grade1,
                Grade2 = Grade2,
                Grade3 = Grade3,
                Grade4 = Grade4,
                Grade5 = Grade5,
                Grade6 = Grade6,
                Percentage = Percentage,
            )
            application.save()
            comment = {
                'Application Saved' : 'All ok'
            }
            Response(comment, status=status.)

        except:
            comment = {
                'Invalid': 'Not Saved In a Model'
            }
            return Response(comment, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def viewApplications(request):
    application = ApplicationForm.objects.all()
    serializer = ApplicationSerializer(application, many=True)
    return Response(serializer.data)