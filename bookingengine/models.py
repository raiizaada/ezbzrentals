from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class BookingRoom(models.Model):
    name= models.CharField(max_length=200) 
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="be_rooms",null=True ,default=None)
    no_of_adult= models.CharField(max_length=20)
    no_of_child= models.CharField(max_length=20)
    max_guest= models.CharField(max_length=200)
    size= models.CharField(max_length=100)
    view= models.CharField(max_length=100)
    bed_types= models.CharField(max_length=100)
    price= models.CharField(max_length=200)
    amenities=models.CharField(max_length=500)
    categories=models.CharField(max_length=500)
    tags=models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "be_rooms" 
    def __str__(self):
        return self.name      



class BookingAmenities(models.Model):
    title=models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    class Meta:  
        db_table = "be_amenities"

    def __str__(self):
        return self.title  
    

class Categories(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=1000,null=True)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    class Meta:  
        db_table = "be_categories"

    def __str__(self):
        return self.name          

class Tags(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=1000,null=True)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    class Meta:  
        db_table = "be_tags"

    def __str__(self):
        return self.name          

class Seasons(models.Model):
    title=models.CharField(max_length=200)
    start_date=models.CharField(max_length=100)
    end_date=models.CharField(max_length=100)
    applied_for_days =models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    class Meta:  
        db_table = "be_seasons"

    def __str__(self):
        return self.start_date          


class Rates(models.Model):
    title=models.CharField(max_length=200)
    rooms=models.ForeignKey(BookingRoom, on_delete=models.CASCADE)
    seasons=models.ForeignKey(Seasons, on_delete=models.CASCADE)
    price_per_night=models.IntegerField()
    description=models.TextField(max_length=1000,null=True)
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    adults = models.CharField(max_length=100,null=True)
    children = models.CharField(max_length=100,null=True)

    def calculate_rate(self, adults):
        total = (float(adults) * self.price_per_night)/100
        total_rate=self.price_per_night+total
        return total_rate

    class Meta:  
        db_table = "be_rates"

    def __str__(self):
        return self.title             

class Services(models.Model):
    title=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    periodicity=models.CharField(max_length=200)
    charge=models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="be_services")
    status = models.BooleanField(default=True)
    user_id = models.IntegerField()
    class Meta:  
        db_table = "be_services"

    def __str__(self):
        return self.title                
    
class RoomsGallery(models.Model):
    image=models.ImageField(upload_to='rooms_gallery')
    user_id = models.IntegerField()
    room_id=models.IntegerField()  
    class Meta:  
        db_table = "be_rooms_gallery"

    def __str__(self):
        return self.image   
    
class Tax(models.Model):
    title=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    amount=models.CharField(max_length=200,null=True)
    per_adult=models.CharField(max_length=200,null=True)
    per_child=models.CharField(max_length=200,null=True)
    limit = models.CharField(max_length=200)
    include = models.BooleanField(default=True)
    rooms=models.CharField(max_length=2000)
    user_id = models.IntegerField()
    status = models.BooleanField(default=True)
    class Meta:  
        db_table = "be_tax"

    def __str__(self):
        return self.title         
    
class Reservation(models.Model):
    User = get_user_model()
    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(BookingRoom, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    booking_id = models.CharField(max_length=100,default="null")

    class Meta:  
        db_table = "be_reservation"

    def __str__(self):
        return self.user
    

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    type=models.CharField(max_length=100)
    coupon_amount =models.CharField(max_length=200,null=True)
    active = models.BooleanField()
    rooms=models.CharField(max_length=2000)
    user_id = models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_coupon"

    def __str__(self):
        return self.code      
    

class SocialMedia(models.Model):
    facebook=models.CharField(max_length=200,null=True,blank=True)
    twitter=models.CharField(max_length=200,null=True,blank=True)
    linkedin=models.CharField(max_length=200,null=True,blank=True)
    instagram=models.CharField(max_length=200,null=True,blank=True)
    youtube=models.CharField(max_length=200,null=True,blank=True)
    user_id = models.IntegerField() 
    status = models.BooleanField(default=True)   

    class Meta:  
        db_table = "be_social_media"

    def __str__(self):
        return self.facebook
    
class ContactInfo(models.Model):
    telephone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    logo=models.ImageField(upload_to='be_property_logo')
    copyright_name=models.CharField(max_length=100)
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_contact_info"

    def __str__(self):
        return self.email
    

class ColorPalettes(models.Model):
    top_background_colour=models.CharField(max_length=100)
    top_font_colour=models.CharField(max_length=100)
    footer_background_colour=models.CharField(max_length=100)
    footer_font_colour=models.CharField(max_length=100)
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_color_palettes"

    def __str__(self):
        return self.top_background_colour    
    
class FooterWidgets(models.Model):
    title=models.CharField(max_length=100) 
    description=models.TextField(max_length=500) 
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_widgets"

    def __str__(self):
        return self.title
    

class BookingInformation(models.Model):
    honorific = models.CharField(max_length=25)
    first_name= models.CharField(max_length=100) 
    last_name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    address= models.TextField(max_length=500)
    zip_code= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    notes= models.TextField(max_length=500)
    card_holder_name= models.CharField(max_length=100)
    credit_card_number= models.CharField(max_length=100)
    expiry_month= models.CharField(max_length=100)
    expiry_year= models.CharField(max_length=100)
    cvv= models.CharField(max_length=100) 
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    room_id = models.CharField(max_length=100)
    adult=models.CharField(max_length=20)
    child=models.CharField(max_length=20)
    no_of_guest=models.CharField(max_length=20)
    no_of_nights=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    tax=models.CharField(max_length=20)
    total_price=models.CharField(max_length=50)
    term_condition=models.BooleanField(default=True)
    user_id = models.IntegerField() 
    extra_services=models.CharField(max_length=1000)
    

    class Meta:  
        db_table = "be_booking_information"

    def __str__(self):
        return self.first_name + self.last_name
    

class RoomAdditionalDetails(models.Model):
    checkin_time=models.CharField(max_length=100)  
    checkout_time=models.CharField(max_length=100)  
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_room_additional_details"

    def __str__(self):
        return self.checkin_time
    
class ExtraService(models.Model):
    title=models.CharField(max_length=200)
    price=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_extra_services"

    def __str__(self):
        return self.title

class TermCondition(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=5000)
    user_id = models.IntegerField()  
    status = models.BooleanField(default=True)

    class Meta:  
        db_table = "be_term&condition"

    def __str__(self):
        return self.title