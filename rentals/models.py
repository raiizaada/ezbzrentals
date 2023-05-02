from pickle import FALSE
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db import models
from django.urls import reverse



# Create your models here.

# user management
class UserProfile(models.Model): 
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserProfile",default=1)
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100) 
    profile_photo=models.FileField(upload_to="user_profile_photo",null=True ,default=None)
    phone=models.CharField(max_length=15)  
    address=models.TextField(null=True, blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=15)
    postal_code=models.IntegerField()  
    property_phone_number=models.CharField(max_length=15)
    tollfree=models.CharField(max_length=15)
    website=models.URLField( max_length=200)
    property_logo=models.FileField(upload_to="profile",null=True ,default=None)
    property_role=models.CharField(max_length=100) 
    no_of_properties=models.CharField(max_length=100) 
    description=models.TextField(max_length=1000)
    status = models.BooleanField(default=True)
   


    class Meta:  
        db_table = "user_profile"

    def __str__(self):
        return self.last_name  


# channels
class Channel(models.Model):  
    channel_title = models.CharField(max_length=100)  
    channel_image=models.FileField(upload_to="channels",null=True ,default=None)
    channel_description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)  
    
  
    class Meta:  
        db_table = "channel"

    def __str__(self):
        return self.channel_title     

# Amenities & Activities

class AmenitiesType(models.Model):
    title=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
   
    class Meta:  
        db_table = "amenities_type"

    def __str__(self):
        return self.title  

class Amenities(models.Model):
    amenities_type=models.ForeignKey(AmenitiesType, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
  
    class Meta:  
        db_table = "amenities"

    def __str__(self):
        return self.title  
       

class Activity(models.Model):  
    name=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True) 
   
    

    class Meta:  
        db_table = "activity"

    def __str__(self):
        return self.name  


class Rentaltype(models.Model):
    room_type_name=models.CharField(max_length=100)
    noof_beds=models.CharField(max_length=10)
    max_occupancy=models.CharField(max_length=10)
    noof_rooms=models.CharField(max_length=10)
    picture=models.FileField(upload_to="roomtype",null=True ,default=None)
    rental_description= models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)

 

    class Meta:  
        db_table = "rental_type"

    def __str__(self):
        return self.room_type_name  


class Taxtype(models.Model):
    taxtype_name=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "tax_type" 

    def __str__(self):
        return self.taxtype_name 

class Tax(models.Model):
    tax_type=models.ForeignKey(Taxtype, on_delete=models.CASCADE)
    tax_name=models.CharField(max_length=100)
    tax_percentage=models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True) 


    class Meta:  
        db_table = "tax" 

    def __str__(self):
        return self.tax_name 


class Policy(models.Model):
    policy_number=models.CharField(max_length=100)
    policy_name=models.CharField(max_length=100)
    policy_type=models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:  
        db_table = "policy" 

    def __str__(self):
        return self.policy_name 


class Ratetype(models.Model):
    ratetype_name=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "rate_type" 

    def __str__(self):
        return self.ratetype_name 


class Rate(models.Model):
    rate_type=models.ForeignKey(Ratetype, on_delete=models.CASCADE)
    rate_name=models.CharField(max_length=100)
    included_occupants=models.CharField(max_length=100)
    extra_adult_charge=models.CharField(max_length=100)
    extra_children_charge=models.CharField(max_length=100)
    weekend_surcharge=models.CharField(max_length=100)
    day_surcharge=models.CharField(max_length=100)
    disable_rates= models.BooleanField(default=FALSE)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "rate" 

    def __str__(self):
        return self.rate_name  


class DiscountType(models.Model):
    discounttype_name=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "discount_type" 

    def __str__(self):
        return self.discounttype_name 

class Discount(models.Model):
    discounts_name=models.CharField(max_length=100)
    discount_type=models.ForeignKey(DiscountType, on_delete=models.CASCADE)
    discounts_amount=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "discount" 

    def __str__(self):
        return self.discounts_name 

class Currency(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    symbol=models.CharField(max_length=100)
    decimal_place=models.CharField(max_length=100)
    currency_value=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "currency" 

    def __str__(self):
        return self.title 

# Rental

class Rental(models.Model):
    rental_name= models.CharField(max_length=20,) 
    rental_short_description=models.TextField(max_length=1000)
    rental_description = models.TextField(max_length=3000)
    cover_image=models.ImageField(upload_to="rentals",null=True ,default=None)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "rental" 
    def __str__(self):
        return self.rental_name      

class RentalBasic(models.Model):
    rental_type=models.CharField(max_length=100)
    rental_basis=models.CharField(max_length=100) 
    floorspace=models.CharField(max_length=100) 
    floorspace_units=models.CharField(max_length=100) 
    grounds=models.CharField(max_length=100) 
    grounds_units=models.CharField(max_length=100) 
    floors_building=models.CharField(max_length=100) 
    entrance=models.CharField(max_length=100) 
    rental_licence=models.CharField(max_length=100)
    user_id = models.IntegerField() 
    rental_id=models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "rental_basic" 

    def __str__(self):
        return str(self.rental_type)


class RentalLocation(models.Model):
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=1000) 
    apartment=models.CharField(max_length=1000) 
    city=models.CharField(max_length=100) 
    state=models.CharField(max_length=100) 
    postal=models.CharField(max_length=100)
    user_id = models.IntegerField() 
    rental_id=models.IntegerField()
    status = models.BooleanField(default=True)
    class Meta:  
        db_table = "rental_location" 

    def __str__(self):
        return str(self.city) 

# invoice
class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField()
    status = models.BooleanField(default=False)
   

    class Meta:  
        db_table = "invoice" 

    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status



class InvoiceItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    user_id = models.IntegerField()
    

    class Meta:  
        db_table = "invoice_item" 
    

    def __str__(self):
        return str(self.customer)

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100) 
    company_logo = models.ImageField(upload_to='company')
    company_email =  models.CharField(max_length=100,null=True, blank=True) 
    company_tel= models.CharField(max_length=15)
    company_address= models.TextField(null=True, blank=True)
    

    class Meta:  
        db_table = "company_profile"

    def __str__(self):
        return str(self.company_name)
      

class RentalAmenities(models.Model):
    amenities=models.CharField(max_length=500)
    user_id = models.IntegerField()
    rental_id=models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "rental_amenities"
        

    def __str__(self):
        return str(self.user_id)

class RentalsGallery(models.Model):
    image=models.ImageField(upload_to='rentals-gallery')
    position = models.PositiveSmallIntegerField(null=True)
    user_id = models.IntegerField()
    rental_id=models.IntegerField()

    class Meta:  
        db_table = "rentals_gallery"
        ordering = ('position',)

    def __str__(self):
        return str(self.image)

class Attributes(models.Model):
    name=models.CharField(max_length=100)
    status = models.BooleanField(default=True)
         

    class Meta:  
        db_table = "attributes"

    def __str__(self):
        return self.name       

     

class Bookings(models.Model):
    rental=models.CharField(max_length=100)
    channel=models.ForeignKey(Channel, on_delete=models.CASCADE)
    booking_type=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100) 
    email=models.CharField(max_length=100) 
    phone=models.CharField(max_length=15)  
    address=models.TextField(null=True, blank=True)
    city=models.CharField(max_length=50,null=True, blank=True)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=15)
    postal_code=models.IntegerField()  
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateField()
   
   
    class Meta:  
        db_table = "bookings" 

    def __str__(self):
        return self.first_name           


class Category(models.Model):
    title = models.CharField(max_length=20,)  
    icon=models.FileField(upload_to="partner_category",null=True ,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)  
    
  
    class Meta:  
        db_table = "partner_category"

    def __str__(self):
        return self.title    


# Partner
class Partner(models.Model):  
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40) 
    subtitle = models.CharField(max_length=40)  
    image=models.FileField(upload_to="partner",null=True ,default=None)
    shortdescription = models.TextField(max_length=250)
    description = models.TextField(max_length=1000)
    url = models.TextField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)  
    
  
    class Meta:  
        db_table = "partner"

    def __str__(self):
        return self.title    


class ChannelManagement(models.Model):
    channels=models.CharField(max_length=500)
    user_id = models.IntegerField()
    rental_id = models.IntegerField(default=True)

    class Meta:  
        db_table = "rental_channel"

    

class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events

class Event(EventAbstract):
    """ Event model """
    User = get_user_model()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rental_id=models.IntegerField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("users:calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("users:calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    class Meta:  
            db_table = "calendar" 


class EventMember(EventAbstract):
    """ Event member model """
    User = get_user_model()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_members"
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)


class Subscription(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    price = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    tenure=models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
  
    class Meta:  
        db_table = "subscription"

    def __str__(self):
        return self.title    

class Country(models.Model):
    name = models.CharField(max_length=200) 
    code=  models.CharField(max_length=200,null=True)
    country_code= models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)  
    
    class Meta:  
        db_table = "country"

    def __str__(self):
        return self.name    

class PropertyRole(models.Model):
    title = models.CharField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)  
    
    class Meta:  
        db_table = "property_role"

    def __str__(self):
        return self.title        


class SubscriptionPlan(models.Model):
    subscription_title = models.CharField(max_length=100)
    price = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    tenure=models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=100)
    user_id=models.IntegerField()
    subscription_id=models.IntegerField()
    status = models.BooleanField(default=True) 
    
  
    class Meta:  
        db_table = "subscription_plan"

    def __str__(self):
        return self.title           

class Roomtype(models.Model):
    title= models.CharField(max_length=100)
    icon=models.FileField(upload_to="roomtype",null=True ,default=None)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:  
        db_table = "room_type"

    def __str__(self):
        return self.title  

class Room(models.Model):
    room_type=models.ForeignKey(Roomtype, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    icon=models.FileField(upload_to="room",null=True ,default=None)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:  
        db_table = "rooms"

    def __str__(self):
        return self.title  
    
     

class Bed(models.Model):
    title= models.CharField(max_length=100)
    icon=models.FileField(upload_to="bed",null=True ,default=None)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:  
        db_table = "bed"

    def __str__(self):
        return self.title  
    


class LongStayDiscount(models.Model):
    seven_nights= models.CharField(max_length=100)
    fourteen_nights= models.CharField(max_length=100)
    twenty_one_nights= models.CharField(max_length=100)
    twenty_eight_nights= models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_longstay_discount"

    def __str__(self):
        return self.seven_nights

class EarlyBirdDiscount(models.Model):
    booking_less= models.CharField(max_length=100)
    booking_less_discount= models.CharField(max_length=100)
    booking_more= models.CharField(max_length=100)
    booking_more_discount= models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_earlybird_discount"

    def __str__(self):
        return self.booking_less        


class HouseRules(models.Model):
    for_kid= models.CharField(max_length=100)
    wheelchair_access= models.CharField(max_length=100)
    parties_allowed= models.CharField(max_length=100)
    smoking_allowed= models.CharField(max_length=100)
    pets= models.CharField(max_length=100)
    house_rules= models.TextField(max_length=3000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_house_rules"

    def __str__(self):
        return self.house_rules        



class RentalPolicy(models.Model):
    name= models.CharField(max_length=1000)
    description= models.TextField(max_length=3000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_policy"

    def __str__(self):
        return self.name        
    
class RentalInstruction(models.Model):
    checkin_instruction= models.CharField(max_length=100)
    checkout_instruction= models.CharField(max_length=100)
    checkin_contact= models.CharField(max_length=100)
    key_collection= models.CharField(max_length=100)
    telephone_country= models.CharField(max_length=100)
    dialing_code= models.CharField(max_length=200,null=True)
    telephone_number= models.CharField(max_length=3000)
    instructions= models.TextField(max_length=3000)
    attach_instruction= models.FileField(upload_to='rentals-instruction')
    checkin_from= models.CharField(max_length=100)
    checkout_until= models.CharField(max_length=100)
    airport_instruction= models.CharField(max_length=100)
    property_directions= models.TextField(max_length=3000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_instruction"

    def __str__(self):
        return self.instructions       


class SeasonalRates(models.Model):
    season_name= models.CharField(max_length=100)
    start_date= models.CharField(max_length=100)
    end_date= models.CharField(max_length=100)
    basic_night= models.CharField(max_length=100)
    weekend_night= models.CharField(max_length=100)
    minimum_stay= models.CharField(max_length=3000)
    maximum_stay= models.CharField(max_length=3000)
    checkin_days= models.CharField(max_length=100,default=True)
    checkout_days= models.CharField(max_length=100,default=True)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_seasonal_rates"

    def __str__(self):
        return self.season_name       

class BasicRates(models.Model):
    currency= models.CharField(max_length=100)
    basic_night= models.CharField(max_length=100)
    weekend_night= models.CharField(max_length=100)
    guest_number= models.CharField(max_length=100)
    minimum_stay= models.CharField(max_length=100)
    maximum_stay= models.CharField(max_length=3000)
    checkin_days= models.CharField(max_length=100,default=True)
    checkout_days= models.CharField(max_length=100,default=True)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_basic_rates"

    def __str__(self):
        return self.currency 


class RentalCleaning(models.Model):
    cleaning_available= models.CharField(max_length=100)
    cleaning_basis= models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_cleaning"

    def __str__(self):
        return self.cleaning_available 

class RentalDeposit(models.Model):
    security_deposit= models.CharField(max_length=100)
    amount= models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_deposit"

    def __str__(self):
        return self.security_deposit 

class RentalTax(models.Model):
    tax_type= models.CharField(max_length=100)
    fee_basis= models.CharField(max_length=100)
    percentage= models.CharField(max_length=100)
    amountin= models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_tax"

    def __str__(self):
        return self.tax_type 

class ExtraServices(models.Model):
    service_name= models.CharField(max_length=100)
    service_provided= models.CharField(max_length=100)
    fee_basis= models.CharField(max_length=100,null=True)
    service_price= models.CharField(max_length=100,null=True)
    earliest_guest_order= models.CharField(max_length=100,null=True)
    latest_guest_order= models.CharField(max_length=100,null=True)
    guest_cancel_order= models.CharField(max_length=100,null=True)
    extra_message=models.TextField(max_length=3000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_extra_services"

    def __str__(self):
        return self.service_name 

class CustomServices(models.Model):
    custom_service_name= models.CharField(max_length=100)
    custom_service_provided= models.CharField(max_length=100)
    custom_fee_basis= models.CharField(max_length=100,null=True)
    custom_service_price= models.CharField(max_length=100,null=True)
    custom_earliest_guest_order= models.CharField(max_length=100,null=True)
    custom_latest_guest_order= models.CharField(max_length=100,null=True)
    custom_guest_cancel_order= models.CharField(max_length=100,null=True)
    custom_extra_message=models.TextField(max_length=3000)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()
    class Meta:  
        db_table = "rental_custom_extra_services"

    def __str__(self):
        return self.custom_service_name         

class OtherRooms(models.Model):
    title=models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "other_rooms"

    def __str__(self):
        return self.title 

class RentalOtherRooms(models.Model):
    other_rooms=models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()    
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "rental_other_rooms"

    def __str__(self):
        return self.other_rooms 


class Services(models.Model):
    title= models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:  
        db_table = "services"

    def __str__(self):
        return self.title        
    

class RentalRoom(models.Model):
    name=models.CharField(max_length=10000)
    no_of_rooms=models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()    
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "rental_rooms"

    def __str__(self):
        return self.name 


class RentalBed(models.Model):
    name=models.CharField(max_length=10000)
    no_of_beds=models.CharField(max_length=100)
    user_id = models.IntegerField()
    rental_id = models.IntegerField()    
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "rental_beds"

    def __str__(self):
        return self.name 