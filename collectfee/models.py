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



# class ApplicationForm(models.Model):
#     #Personal Details
#     FirstName = models.CharField(max_length=100, null=True)
#     MiddleName = models.CharField(max_length=100, null=True)
#     LastName = models.CharField(max_length=100, null=True)
#     Aadhaar = models.IntegerField(null=True)
#     Martial = models.IntegerField(null=True)
#     Mobile = models.IntegerField(null=True)
#     Email = models.EmailField(null=True)
#     MotherName = models.CharField(max_length=100, null=True)
#     FatherName = models.CharField(max_length=100, null=True)
#     AnnualIncome = models.IntegerField(null=True)
#     AnyOtherUni= models.CharField(max_length=100, null=True)
#     #Address
#     Address = models.CharField(max_length=100, null=True)
#     Pincode = models.IntegerField(null=True)
#     Category = models.CharField(max_length=100, null=True)
#     Minority = models.CharField(max_length=100, null=True)
#     State = models.CharField(max_length=100, null=True) 
#     City = models.CharField(max_length=100, null=True)
#     DateOfBirth = models.DateField(null=True)
#     Nationality = models.CharField(max_length=100, null=True)
   
#     #Extra Details
#     PayingGuest = models.CharField(max_length=100, null=True)
#     Transport = models.CharField(max_length=100, null=True)

#     #Subjects
#     Elective1 = models.CharField(max_length=100, null=True)
#     Elective2 = models.CharField(max_length=100, null=True)
#     Elective3 = models.CharField(max_length=100, null=True)

#     Preference1 = models.CharField(max_length=100, null=True)
#     Preference2 = models.CharField(max_length=100, null=True)
#     Preference3 = models.CharField(max_length=100, null=True)

    
#     Employment = models.CharField(max_length=100, null=True)
    
    
#     FullMarks1 = models.IntegerField(null=True)
#     FullMarks2 = models.IntegerField(null=True)
#     FullMarks3 = models.IntegerField(null=True)
#     FullMarks4 = models.IntegerField(null=True)
#     FullMarks5 = models.IntegerField(null=True)
#     FullMarks6 = models.IntegerField(null=True)

#     MarkObtain1 = models.IntegerField(null=True)
#     MarkObtain2 = models.IntegerField(null=True)
#     MarkObtain3 = models.IntegerField(null=True)
#     MarkObtain4 = models.IntegerField(null=True)
#     MarkObtain5 = models.IntegerField(null=True)
#     MarkObtain6 = models.IntegerField(null=True)

#     Grade1 = models.CharField(max_length=100, null=True)
#     Grade2 = models.CharField(max_length=100, null=True)
#     Grade3 = models.CharField(max_length=100, null=True)
#     Grade4 = models.CharField(max_length=100, null=True)
#     Grade5 = models.CharField(max_length=100, null=True)
#     Grade6 = models.CharField(max_length=100, null=True)
#     Percentage = models.FloatField(null=True)





class ApplicationForm(models.Model):
    #Personal Details
    firstName = models.CharField(max_length=100, null=True, blank=True)
    middleName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    aadhaar = models.IntegerField(null=True, blank=True)
    martial = models.CharField(max_length= 200, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    motherName = models.CharField(max_length=100, null=True, blank=True)
    fatherName = models.CharField(max_length=100, null=True, blank=True)
    annualIncome = models.IntegerField(null=True, blank=True)
    anyotheruni= models.CharField(max_length=100, null=True, blank=True)
    #Address
    address = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    minority = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True) 
    city = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
   
    #Extra Details
    payingguest = models.CharField(max_length=100, null=True, blank=True)
    transport = models.CharField(max_length=100, null=True, blank=True)

    #Subjects
    elective1 = models.CharField(max_length=100, null=True, blank=True)
    elective2 = models.CharField(max_length=100, null=True, blank=True)
    elective3 = models.CharField(max_length=100, null=True, blank=True)

    preference1 = models.CharField(max_length=100, null=True, blank=True)
    preference2 = models.CharField(max_length=100, null=True, blank=True)
    preference3 = models.CharField(max_length=100, null=True, blank=True)

    
    employment = models.CharField(max_length=100, null=True, blank=True)
    
    
    fullmarks1 = models.IntegerField(null=True, blank=True)
    fullmarks2 = models.IntegerField(null=True, blank=True)
    fullmarks3 = models.IntegerField(null=True, blank=True)
    fullmarks4 = models.IntegerField(null=True, blank=True)
    fullmarks5 = models.IntegerField(null=True, blank=True)
    fullmarks6 = models.IntegerField(null=True, blank=True)

    markObtain1 = models.IntegerField(null=True, blank=True)
    markObtain2 = models.IntegerField(null=True, blank=True)
    markObtain3 = models.IntegerField(null=True, blank=True)
    markObtain4 = models.IntegerField(null=True, blank=True)
    markObtain5 = models.IntegerField(null=True, blank=True)
    markObtain6 = models.IntegerField(null=True, blank=True)

    grade1 = models.CharField(max_length=100, null=True, blank=True)
    grade2 = models.CharField(max_length=100, null=True, blank=True)
    grade3 = models.CharField(max_length=100, null=True, blank=True)
    grade4 = models.CharField(max_length=100, null=True, blank=True)
    grade5 = models.CharField(max_length=100, null=True, blank=True)
    grade6 = models.CharField(max_length=100, null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)

    


