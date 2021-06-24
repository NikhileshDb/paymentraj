from django.db import models

# Create your models here.
class Order(models.Model):
    order_product = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_product



class ApplicationForm(models.Model):
    #Personal Details
    FirstName = models.CharField(max_length=100, null=True)
    MiddleName = models.CharField(max_length=100, null=True)
    LastName = models.CharField(max_length=100, null=True)
    Aadhaar = models.IntegerField(null=True)
    Martial = models.IntegerField(null=True)
    Mobile = models.IntegerField(null=True)
    Email = models.EmailField(null=True)
    MotherName = models.CharField(max_length=100, null=True)
    FatherName = models.CharField(max_length=100, null=True)
    AnnualIncome = models.IntegerField(null=True)
    AnyOtherUni= models.CharField(max_length=100, null=True)
    #Address
    Address = models.CharField(max_length=100, null=True)
    Pincode = models.IntegerField(null=True)
    Category = models.CharField(max_length=100, null=True)
    Minority = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True) 
    City = models.CharField(max_length=100, null=True)
    DateOfBirth = models.DateField(null=True)
    Nationality = models.CharField(max_length=100, null=True)
   
    #Extra Details
    PayingGuest = models.CharField(max_length=100, null=True)
    Transport = models.CharField(max_length=100, null=True)

    #Subjects
    Elective1 = models.CharField(max_length=100, null=True)
    Elective2 = models.CharField(max_length=100, null=True)
    Elective3 = models.CharField(max_length=100, null=True)

    Preference1 = models.CharField(max_length=100, null=True)
    Preference2 = models.CharField(max_length=100, null=True)
    Preference3 = models.CharField(max_length=100, null=True)

    
    Employment = models.CharField(max_length=100, null=True)
    
    
    FullMarks1 = models.IntegerField(null=True)
    FullMarks2 = models.IntegerField(null=True)
    FullMarks3 = models.IntegerField(null=True)
    FullMarks4 = models.IntegerField(null=True)
    FullMarks5 = models.IntegerField(null=True)
    FullMarks6 = models.IntegerField(null=True)

    MarkObtain1 = models.IntegerField(null=True)
    MarkObtain2 = models.IntegerField(null=True)
    MarkObtain3 = models.IntegerField(null=True)
    MarkObtain4 = models.IntegerField(null=True)
    MarkObtain5 = models.IntegerField(null=True)
    MarkObtain6 = models.IntegerField(null=True)

    Grade1 = models.CharField(max_length=100, null=True)
    Grade2 = models.CharField(max_length=100, null=True)
    Grade3 = models.CharField(max_length=100, null=True)
    Grade4 = models.CharField(max_length=100, null=True)
    Grade5 = models.CharField(max_length=100, null=True)
    Grade6 = models.CharField(max_length=100, null=True)
    Percentage = models.FloatField(null=True)

    
    


