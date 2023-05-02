from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookingengine.models import BookingAmenities, BookingInformation, BookingRoom, Categories, ColorPalettes, ContactInfo, Coupon, ExtraService, FooterWidgets, Rates, Reservation, RoomsGallery, Seasons, Services, SocialMedia, Tags,Tax, TermCondition
from rentals.models import  Bookings, Country, PropertyRole, Rental, UserProfile
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import authenticate, login, logout
from users.tokens import generate_token
import datetime
import ast
from django.views.decorators.csrf import csrf_exempt
import json




# Create your views here.

# Dashboard Code start

def index(request):
    rentalCount=Rental.objects.filter(user_id=request.user.id).count()
    bookingCount=Bookings.objects.filter(user_id=request.user.id).count()
    bookingengine=Bookings.objects.filter(user_id=request.user.id)
    context={
        "rentalCount":rentalCount,
        "bookingCount":bookingCount,
        "bookingengine":bookingengine
    }
    return render(request,'bookingengine/dashboard/dashboard.html',context)

# Dashboard Code end       

# Authentication Code start

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/booking-engine/signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/booking-engine/signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/booking-engine/signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/booking-engine/signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/booking-engine/signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_superuser=False
        myuser.is_staff=True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        LastInsertId = (User.objects.last()).id
        LastRow = User.objects.get(id=LastInsertId)
        UserProfiles = UserProfile() 
        UserProfiles.first_name = 'NA'
        UserProfiles.last_name = 'NA'
        UserProfiles.phone = 'NA'
        UserProfiles.address = 'NA'
        UserProfiles.city= 'NA'
        UserProfiles.state='NA'
        UserProfiles.country = 'NA'
        UserProfiles.postal_code = '201308'
        UserProfiles.property_phone_number = 'NA'
        UserProfiles.tollfree = 'NA'
        UserProfiles.website = 'NA'
        UserProfiles.property_logo = 'NA'
        UserProfiles.status = '1'
        UserProfiles.user_id =  LastRow.id           
        UserProfiles.save()
        return redirect('/booking-engine/signin')
    return render(request,'bookingengine/authentication/signup.html')

        
    

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('/booking-engine/dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username,password=password)
            
            if user.is_staff:
                login(request,user)
                return redirect('/booking-engine/dashboard')
            
            else:
                messages.success(request,"Incorrect username or password.")
                return redirect('/booking-engine/signup')
        response = render(request,'bookingengine/authentication/signin.html')
        return HttpResponse(response)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/booking-engine/signin')   

# Authentication Code end

# Room Code Start
@login_required(login_url='/bookingengine/')
def room_insert(request):
    if request.method == "POST": 
        room=BookingRoom()
        room.name=request.POST.get('name')
        room.no_of_adult=request.POST.get('no_of_adult')
        room.no_of_child=request.POST.get('no_of_child')
        room.max_guest=request.POST.get('max_guest')
        room.image=request.FILES.get('image')
        room.price=request.POST.get('price')
        room.size=request.POST.get('size')
        room.view=request.POST.get('view')
        room.amenities=request.POST.getlist('amenities[]')
        room.categories=request.POST.get('categories')
        room.tags=request.POST.get('tags')
        room.bed_types=request.POST.get('bed_types')
        room.description=request.POST.get('description')
        room.status=request.POST.get('status')
        room.user_id=request.user.id
        room.save()
        messages.success(request, ' Row added Successfully.')
    return redirect ('/booking-engine/rooms')

    

@login_required(login_url='/booking-engine/')     
def room_add(request):
    category=Categories.objects.filter(user_id=request.user.id)
    tag=Tags.objects.filter(user_id=request.user.id)
    amenities=BookingAmenities.objects.filter(user_id=request.user.id)
    context={
        'category':category,
        'tag':tag,
        'amenities':amenities
    }
    return render(request,"bookingengine/rentals/room-add.html",context)  

# @login_required(login_url='/booking-engine/')
def rooms(request):  
    room = BookingRoom.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/rentals/rooms.html",{'room':room})  

@login_required(login_url='/booking-engine/')
def room_edit(request, id):  
    room= BookingRoom.objects.get(id=id) 
    category=Categories.objects.filter(user_id=request.user.id)
    tag=Tags.objects.filter(user_id=request.user.id)
    amenities=BookingAmenities.objects.filter(user_id=request.user.id) 
    context={
        'category':category,
        'tag':tag,
        'amenities':amenities,
        'room':room
    }
    return render(request,'bookingengine/rentals/room-edit.html',context)  

@login_required(login_url='/booking-engine/')
def room_update(request, id):    
    if request.method == "POST": 
        room= BookingRoom.objects.get(id=id)
        room.name=request.POST.get('name')
        room.no_of_adult=request.POST.get('no_of_adult')
        room.no_of_child=request.POST.get('no_of_child')
        room.max_guest=request.POST.get('max_guest')
        if 'image' in request.FILES:
           room.image = request.FILES['image']
        room.size=request.POST.get('size')
        room.view=request.POST.get('view')
        room.amenities=request.POST.getlist('amenities[]')
        room.categories=request.POST.get('categories')
        room.tags=request.POST.get('tags')
        room.bed_types=request.POST.get('bed_types')
        room.description=request.POST.get('description')
        room.status=request.POST.get('status')
        room.save()
        messages.success(request, ' Row Updated Successfully.')
        return redirect ('/booking-engine/rooms')
   
    return render(request, 'bookingengine/rentals/room-edit.html', {'room': room})  

@login_required(login_url='/booking-engine/')
def room_destroy(request, id):  
    room = BookingRoom.objects.get(id=id)  
    room.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/booking-engine/rooms")

# Room Code end
  
# Amenities code start
@login_required(login_url='/booking-engine/')
def amenities_insert(request):  
    if request.method == "POST":
        amenities=BookingAmenities()
        amenities.title=request.POST.get('title')  
        amenities.user_id=request.user.id
        amenities.status=request.POST.get('status')
        amenities.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/amenities')   

@login_required(login_url='/booking-engine/')
def amenities_add(request):
    return render (request,"bookingengine/amenities/amenities-add.html")     
       
@login_required(login_url='/booking-engine/')
def amenities(request):  
    amenities = BookingAmenities.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/amenities/amenities.html",{'amenities':amenities})  

@login_required(login_url='/booking-engine/')
def amenities_edit(request, id):  
    amenities = BookingAmenities.objects.get(id=id)  
    return render(request,'bookingengine/amenities/amenities-edit.html', {'amenities':amenities})  

@login_required(login_url='/booking-engine/')
def amenities_update(request, id):  
    amenities = BookingAmenities.objects.get(id=id) 
    if request.method == "POST":
        amenities.title=request.POST.get('title')  
        amenities.status=request.POST.get('status')
        amenities.save()
        messages.success(request, ' Row updated Successfully.')

    return redirect('/booking-engine/amenities')  
   

@login_required(login_url='/booking-engine/')
def amenities_destroy(request, id):  
    amenities = BookingAmenities.objects.get(id=id)  
    amenities.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/amenities')  
# Amenities code end      

# Category code start
@login_required(login_url='/booking-engine/')
def category_insert(request):  
    if request.method == "POST":
        category=Categories()
        category.name=request.POST.get('name') 
        category.description=request.POST.get('description')  
        category.user_id=request.user.id
        category.status=request.POST.get('status')
        category.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/categories')   

@login_required(login_url='/booking-engine/')
def category_add(request):
    return render (request,"bookingengine/categories/category-add.html")     
       
@login_required(login_url='/booking-engine/')
def category(request):  
    category = Categories.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/categories/category.html",{'category':category})  

@login_required(login_url='/booking-engine/')
def category_edit(request, id):  
    category = Categories.objects.get(id=id)  
    return render(request,'bookingengine/categories/category-edit.html', {'category':category})  

@login_required(login_url='/booking-engine/')
def category_update(request, id):  
    category = Categories.objects.get(id=id) 
    if request.method == "POST":
        category=Categories.objects.get(id=id)  
        category.name=request.POST.get('name') 
        category.description=request.POST.get('description')  
        category.status=request.POST.get('status')
        category.save()
        messages.success(request, ' Row updated Successfully.')

    return redirect('/booking-engine/categories') 

@login_required(login_url='/booking-engine/')
def category_destroy(request, id):  
    category = Categories.objects.get(id=id)  
    category.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/categories') 

# Category code end    

# Tag code start
@login_required(login_url='/booking-engine/')
def tag_insert(request):  
    if request.method == "POST":
        tag=Tags()
        tag.name=request.POST.get('name') 
        tag.description=request.POST.get('description')  
        tag.user_id=request.user.id
        tag.status=request.POST.get('status')
        tag.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/tags')   

@login_required(login_url='/booking-engine/')
def tag_add(request):
    return render (request,"bookingengine/tags/tag-add.html")     
       
@login_required(login_url='/booking-engine/')
def tag(request):  
    tag = Tags.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/tags/tags.html",{'tag':tag})  

@login_required(login_url='/booking-engine/')
def tag_edit(request, id):  
    tag = Tags.objects.get(id=id)  
    return render(request,'bookingengine/tags/tag-edit.html', {'tag':tag})  

@login_required(login_url='/booking-engine/')
def tag_update(request, id):  
    if request.method == "POST":
        tag=Tags.objects.get(id=id)  
        tag.name=request.POST.get('name') 
        tag.description=request.POST.get('description')  
        tag.status=request.POST.get('status')
        tag.save()
        messages.success(request, ' Row updated Successfully.')

    return redirect('/booking-engine/tags') 

@login_required(login_url='/booking-engine/')
def tag_destroy(request, id):  
    tag = Tags.objects.get(id=id)  
    tag.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/tags') 

# Tag code end   

# Season code start
@login_required(login_url='/booking-engine/')
def season_insert(request):  
    if request.method == "POST":
        season=Seasons()
        season.title=request.POST.get('title')   
        season.start_date=request.POST.get('start_date') 
        season.end_date=request.POST.get('end_date') 
        season.applied_for_days=request.POST.getlist('applied_for_days[]') 
        season.user_id=request.user.id
        season.status=request.POST.get('status')
        season.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/seasons')   

@login_required(login_url='/booking-engine/')
def season_add(request):
    return render (request,"bookingengine/seasons/season-add.html")     
       
@login_required(login_url='/booking-engine/')
def seasons(request):  
    season = Seasons.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/seasons/seasons.html",{'season':season})  

@login_required(login_url='/booking-engine/')
def season_edit(request, id):  
    season = Seasons.objects.get(id=id)  
    return render(request,'bookingengine/seasons/season-edit.html', {'season':season})  

@login_required(login_url='/booking-engine/')
def season_update(request, id):  
    if request.method == "POST":
        season=Seasons.objects.get(id=id)
        season.title=request.POST.get('title')   
        season.start_date=request.POST.get('start_date') 
        season.end_date=request.POST.get('end_date') 
        season.applied_for_days=request.POST.getlist('applied_for_days[]') 
        season.user_id=request.user.id
        season.status=request.POST.get('status')
        season.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/seasons')  
@login_required(login_url='/booking-engine/')
def season_destroy(request, id):  
    season = Seasons.objects.get(id=id)  
    season.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/seasons') 

# Season code end   

# Rate code start
@login_required(login_url='/booking-engine/')
def rate_insert(request):  
    if request.method == "POST":
        rate=Rates()
        rate.title=request.POST.get('title')   
        rate.rooms_id=request.POST.get('rooms') 
        rate.seasons_id=request.POST.get('seasons')
        rate.price_per_night="" 
        rate.adults=""
        rate.children=""
        rate.description=request.POST.get('description') 
        rate.user_id=request.user.id
        rate.status=request.POST.get('status')
        rate.save()
        LastInsertId = (Rates.objects.last()).id
        LastRow = Rates.objects.get(id=LastInsertId)
        path1 ="/booking-engine/rate-edit/"
        path2=str(LastInsertId)
        path = path1+path2
    messages.success(request, 'Row updated Successfully.')
    return HttpResponseRedirect(path)
        
      

def calculate_booking_rate(request):
    if request.method == 'GET':
        booking_rate = Rates.objects.first()
        num_adults = int(request.GET.get('num_adults', 0))
        num_children = int(request.GET.get('num_children', 0))
        total_rate = (num_adults * booking_rate.adult_rate) + (num_children * booking_rate.child_rate)
        return JsonResponse(str(total_rate), safe=False) 
    

@login_required(login_url='/booking-engine/')
def rate_add(request):
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    seasons=Seasons.objects.filter(user_id=request.user.id)
    context={
        'rooms':rooms,
        'seasons':seasons
    }
    return render (request,"bookingengine/rates/rate-add.html",context)     
       
@login_required(login_url='/booking-engine/')
def rates(request):  
    rate = Rates.objects.filter(user_id=request.user.id)
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    seasons=Seasons.objects.filter(user_id=request.user.id)
    
    context={
        'rooms':rooms,
        'seasons':seasons,
        'rate':rate
    }
    return render(request,"bookingengine/rates/rates.html",context)  

@login_required(login_url='/booking-engine/')
def rate_edit(request, id):  
    rate = Rates.objects.get(id=id)
    rates=rate.calculate_rate(rate.adults) 
    print(rates)
    rooms=BookingRoom.objects.all()
    seasons=Seasons.objects.all()
    context={
        'rooms':rooms,
        'seasons':seasons,
        'rate':rate,
        'rates':rates
    } 
    return render(request,'bookingengine/rates/rate-edit.html', context)  

@login_required(login_url='/booking-engine/')
def rate_update(request, id):  
    if request.method == "POST":
        rate=Rates.objects.get(id=id) 
        rate.price_per_night=request.POST.get('price_per_night') 
        rate.adults=request.POST.get('adults') 
        rate.children=request.POST.get('children') 
        rate.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/rates') 
  
@login_required(login_url='/booking-engine/')
def rate_destroy(request, id):  
    rate = Rates.objects.get(id=id)  
    rate.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/rates') 

# Rate code end   

# Services code start
@login_required(login_url='/booking-engine/')
def service_insert(request):  
    if request.method == "POST":
        service=Services()
        service.title=request.POST.get('title')   
        service.price=request.POST.get('price') 
        service.periodicity=request.POST.get('periodicity') 
        service.charge=request.POST.get('charge') 
        service.featured_image=request.FILES.get('featured_image') 
        service.user_id=request.user.id
        service.status=request.POST.get('status')
        service.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/services')   

@login_required(login_url='/booking-engine/')
def service_add(request):
    return render (request,"bookingengine/services/service-add.html")     
       
@login_required(login_url='/booking-engine/')
def services(request):  
    service = Services.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/services/services.html",{'service':service})  

@login_required(login_url='/booking-engine/')
def service_edit(request, id):  
    service = Services.objects.get(id=id)  
    return render(request,'bookingengine/services/service-edit.html', {'service':service})  

@login_required(login_url='/booking-engine/')
def service_update(request, id):  
    if request.method == "POST":
        service=Services.objects.get(id=id)
        service.title=request.POST.get('title')   
        service.price=request.POST.get('price') 
        service.periodicity=request.POST.get('periodicity') 
        service.charge=request.POST.get('charge') 
        if 'featured_image' in request.FILES:
           service.featured_image= request.FILES['featured_image']
        service.user_id=request.user.id
        service.status=request.POST.get('status')
        service.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/booking-engine/services') 
    
@login_required(login_url='/booking-engine/')
def service_destroy(request, id):  
    service = Services.objects.get(id=id)  
    service.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/services') 

# Service code end 

#Profile Code start
def profile(request):
    bookingengine = UserProfile.objects.get(user_id=request.user.id) 
    country=Country.objects.all()
    propertyrole=PropertyRole.objects.all()
    context={
        'bookingengine':bookingengine,
        'country':country,
        'propertyrole':propertyrole
    }
    return render(request,"bookingengine/user/profile.html",context)  

def profile_update(request,id):
    if request.method == "POST":
        bookingengine = UserProfile.objects.get(id=id)
        bookingengine.first_name =  request.POST.get('first_name')
        bookingengine.last_name =  request.POST.get('last_name')
        bookingengine.phone =  request.POST.get('phone')
        bookingengine.address =  request.POST.get('address')
        bookingengine.city=  request.POST.get('city')
        bookingengine.state= request.POST.get('state')
        bookingengine.country =  request.POST.get('country')
        bookingengine.postal_code =  request.POST.get('postal_code')
        bookingengine.property_phone_number =  request.POST.get('property_phone_number')
        bookingengine.tollfree =  request.POST.get('tollfree')
        bookingengine.website =  request.POST.get('website')
        bookingengine.property_role =  request.POST.get('property_role')
        bookingengine.no_of_properties =  request.POST.get('no_of_properties')
        bookingengine.description =  request.POST.get('description')   
        bookingengine.save()
        messages.success(request, 'Row updated Successfully.')
        return redirect ('/booking-engine/profile')

#Profile Code end
    
# Gallery Code start    
def rooms_gallery(request,id):
    room=BookingRoom.objects.get(id=id)
    gallery=RoomsGallery.objects.filter(room_id=room.id)
    context={
        'room':room,
        'gallery':gallery
    }
    return render(request,'bookingengine/rentals/rooms-gallery.html',context)   

def rooms_gallery_insert(request,id):
    if request.method == "POST":
        rentals_gallery=RoomsGallery()
        rentals_gallery.image=request.FILES.get('image')
        rentals_gallery.user_id=request.user.id
        rentals_gallery.room_id=id
        rentals_gallery.save()
        rental=rentals_gallery.save()
        data = {'is_valid': True, 'name': rental.image.name, 'url': rental.image.url}
    else:
        data = {'is_valid': False}
    messages.success(request, ' Row Updated Successfully.')
    return JsonResponse(data)

def gallery_destroy(request, id):  
    gallery = RoomsGallery.objects.get(id=id)  
    gallery.delete() 
    messages.success(request, ' Row deleted Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))   

# Gallery Code end  

# Tax code start
@login_required(login_url='/booking-engine/')
def tax_insert(request):  
    if request.method == "POST":
        tax=Tax()
        tax.title=request.POST.get('title')   
        tax.type=request.POST.get('type') 
        tax.amount=request.POST.get('amount') 
        tax.per_adult=request.POST.get('per_adult') 
        tax.per_child=request.POST.get('per_child') 
        tax.limit=request.POST.get('limit') 
        tax.include=request.POST.get('include') 
        tax.rooms=request.POST.getlist('rooms[]') 
        tax.user_id=request.user.id
        tax.status=request.POST.get('status')
        tax.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/tax')   

@login_required(login_url='/booking-engine/')
def tax_add(request):
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    context={
      'rooms':rooms  
    }
    return render (request,"bookingengine/tax/tax-add.html",context)    

@login_required(login_url='/booking-engine/')
def tax(request):  
    tax = Tax.objects.filter(user_id=request.user.id)
    context={
      'tax':tax,
    }
    return render(request,"bookingengine/tax/tax.html",context) 

@login_required(login_url='/booking-engine/')
def tax_edit(request,id):  
    tax = Tax.objects.get(id=id)
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    context={
      'tax':tax,
       'rooms':rooms  
    }
    return render(request,"bookingengine/tax/tax-edit.html",context) 

@login_required(login_url='/booking-engine/')
def tax_update(request,id):  
    if request.method == "POST":
        tax=Tax.objects.get(id=id)
        tax.title=request.POST.get('title')   
        tax.type=request.POST.get('type') 
        tax.amount=request.POST.get('amount') 
        tax.per_adult=request.POST.get('per_adult') 
        tax.per_child=request.POST.get('per_child') 
        tax.limit=request.POST.get('limit') 
        tax.rooms=request.POST.getlist('rooms[]') 
        tax.include=request.POST.get('include') 
        tax.rooms=request.POST.get('rooms') 
        tax.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/booking-engine/tax') 

@login_required(login_url='/booking-engine/')
def tax_destroy(request,id): 
    tax=Tax.objects.get(id=id)
    tax.delete()
    return redirect('/booking-engine/tax')

#Tax Code end
@login_required(login_url='/booking-engine/')
def overview (request):
    if request.method =="GET":
        try:
            rr = []
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.GET.get('checkin_date')) and str(each_reservation.check_out) < str(request.GET.get('checkout_date')):
                    pass
                elif str(each_reservation.check_in) > str(request.GET.get('checkin_date')) and str(each_reservation.check_out) > str(request.GET.get('checkout_date')):
                    pass
                else:
                    rr.append(each_reservation.room.id)
            checkin=request.GET.get('checkin_date')
            checkout=request.GET.get('checkout_date') 
            request.session['checkin'] = checkin
            request.session['checkout'] = checkout     
            child=int(request.GET.get('no_of_child'))
            adult=int(request.GET.get('no_of_adult')) 
            request.session['child'] = child
            request.session['adult'] = adult    
            no_of_guest= child + adult   
            request.session['no_of_guest'] = no_of_guest    
            room = BookingRoom.objects.all().filter(max_guest__gte=adult + child,user_id=request.user.id).exclude(id__in=rr)
            
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'flag':True,'checkin':checkin,
                'checkout':checkout,
                'child':child,
                'adult':adult,
                "no_of_guest":no_of_guest}
           
            response = render(request,'bookingengine/rentals/overview.html',data)
        except Exception as e:
            messages.error(request,e)
            response = render(request,'bookingengine/rentals/overview.html')
    return HttpResponse(response)

def overview_all(request):
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    return render(request,'bookingengine/rentals/overview.html',{'rooms':rooms})

def overview_grid(request):
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    return render(request,'bookingengine/rentals/overview-grid.html',{'rooms':rooms})

def room_details(request,id):
    rooms=BookingRoom.objects.get(id=id,user_id=request.user.id)
    my_list = (rooms.amenities)
    my_lists = ast.literal_eval(my_list)
    room=BookingRoom.objects.filter(user_id=request.user.id)
    gallery=RoomsGallery.objects.filter(room_id=rooms.id)
    return render(request,'bookingengine/rentals/room-details.html',{'rooms':rooms,'gallery':gallery,'room':room,'my_lists':my_lists})

@login_required(login_url='/booking-engine/')
def book_room(request):
    if request.method =="POST":
        room_id = request.POST['room_id']       
        room = BookingRoom.objects.all().get(id=room_id)
        #for finding the reserved rooms on this time period for excluding from the query set
        for each_reservation in Reservation.objects.all().filter(room = room):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request,"Sorry This Room is unavailable for Booking")
                return redirect("homepage")
            
        current_user = request.user
        total_person = int( request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        room_object = BookingRoom.objects.all().get(id=room_id)
        room_object.status = '2'
        
        user_object = User.objects.all().get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        person = total_person
        reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']

        reservation.save()

        messages.success(request,"Congratulations! Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')
    

@login_required(login_url='/booking-engine/')
def book_room_page(request):
    room = BookingRoom.objects.all().get(id=int(request.GET['roomid']))
    tax=Tax.objects.get(user_id=request.user.id)
    my_list = (room.amenities)
    my_lists = ast.literal_eval(my_list)
    tc=TermCondition.objects.filter(user_id=request.user.id)
    extra_service=ExtraService.objects.filter(user_id=request.user.id)
    return HttpResponse(render(request,'bookingengine/bookings/bookroom.html',{'tc':tc,'room':room,'tax':tax,'my_lists':my_lists,'extra_service':extra_service}))    


@csrf_exempt
def get_session_data(request):
    checkin = request.session.get('checkin')
    checkout = request.session.get('checkout')
    adult = request.session.get('adult')
    child = request.session.get('child')
    no_of_guest=request.session.get('no_of_guest')
   
    context={
         'checkin':checkin,
         'checkout':checkout,
         'no_of_guest':no_of_guest, 
         'adult':adult,
         'child':child 
     }
    json_data = json.dumps(context)  # Serialize data as JSON
    return HttpResponse(json_data, content_type='application/json')
    
   
# Coupon Code start
@login_required(login_url='/booking-engine/')
def coupon_insert(request):  
    if request.method == "POST":
        coupon=Coupon()
        coupon.code=request.POST.get('code')   
        coupon.valid_from=request.POST.get('valid_from') 
        coupon.valid_to=request.POST.get('valid_to')
        coupon.type=request.POST.get('type') 
        coupon.coupon_amount=request.POST.get('coupon_amount') 
        coupon.rooms=request.POST.getlist('rooms[]') 
        coupon.user_id=request.user.id
        coupon.active=request.POST.get('active')
        coupon.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/coupons')   

@login_required(login_url='/booking-engine/')
def coupon_add(request):
    rooms=BookingRoom.objects.filter(user_id=request.user.id)
    return render (request,"bookingengine/coupons/coupon-add.html",{'rooms':rooms})     
       
@login_required(login_url='/booking-engine/')
def coupons(request):  
    coupon = Coupon.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/coupons/coupons.html",{'coupon':coupon,})  

@login_required(login_url='/booking-engine/')
def coupon_edit(request, id):  
    coupon = Coupon.objects.get(id=id) 
    rooms=BookingRoom.objects.filter(user_id=request.user.id) 
    return render(request,'bookingengine/coupons/coupon-edit.html', {'coupon':coupon,'rooms':rooms})  

@login_required(login_url='/booking-engine/')
def coupon_update(request, id):  
    if request.method == "POST":
        coupon=Coupon.objects.get(id=id)
        coupon.code=request.POST.get('code')   
        coupon.valid_from=request.POST.get('valid_from') 
        coupon.valid_to=request.POST.get('valid_to')
        coupon.type=request.POST.get('type') 
        coupon.coupon_amount=request.POST.get('coupon_amount') 
        coupon.rooms=request.POST.getlist('rooms[]') 
        coupon.user_id=request.user.id
        coupon.active=request.POST.get('active')
        coupon.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/booking-engine/coupons') 
    
@login_required(login_url='/booking-engine/')
def coupon_destroy(request, id):  
    coupon = Coupon.objects.get(id=id)  
    coupon.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/coupons') 

# Coupon Code end 


# @require_POST
# def coupon_apply(request):
#     now=timezone.now()
#     form=CouponApplyForm(request.POST)
#     if form.is_valid():
#         code=form.cleaned_data['code']
#         try:
#             coupon=Coupon.objects.get(code__iexact=code,
#                                       valid_from__lte=now,
#                                       valid_to__gte=now,
#                                       active=True)
#             request.session['coupon_id']=coupon.id
#         except coupon.DoesNotExist:
#             request.session['coupon_id']=None

@login_required(login_url='/booking-engine/')
def preview(request,id):
    room=BookingRoom.objects.get(id=id,user_id=request.user.id)
    my_list = (room.amenities)
    my_lists = ast.literal_eval(my_list)
    tax=Tax.objects.filter(user_id=request.user.id)
    gallery=RoomsGallery.objects.filter(room_id=room.id)
    profile=UserProfile.objects.get(user_id=request.user.id)
  

    context={
        'room':room,
        'tax':tax,
        'gallery':gallery,
        'profile':profile,
        'my_lists':my_lists
               
        
    }

    return render(request,'bookingengine/rentals/preview.html',context)


def social_media_view(request):
    
    try:
        social_media = SocialMedia.objects.get(user_id=request.user.id)
        created = False
    except SocialMedia.DoesNotExist:
        social_media = SocialMedia(user_id=request.user.id)
        created = True

    if request.method == 'POST':
        social_media.facebook = request.POST['facebook']
        social_media.twitter = request.POST['twitter']
        social_media.linkedin = request.POST['linkedin']
        social_media.instagram = request.POST['instagram']
        social_media.youtube = request.POST['youtube']
        social_media.user_id = request.user.id
        social_media.status = request.POST['status']
        social_media.save()
        messages.success(request, ' Data added Successfully.')

        if created:
           return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'bookingengine/settings/social-media.html', {'social_media': social_media})



def contact_info_view(request):
    
    try:
        contact = ContactInfo.objects.get(user_id=request.user.id)
        created = False
    except ContactInfo.DoesNotExist:
        contact = ContactInfo(user_id=request.user.id)
        created = True

    if request.method == 'POST':
        contact.telephone = request.POST['telephone']
        contact.email = request.POST['email']
        contact.address = request.POST['address']
        contact.user_id = request.user.id
        if 'logo' in request.FILES:
           contact.logo=request.FILES['logo']
        contact.copyright_name=request.POST['copyright_name']
        contact.status = request.POST['status']
        contact.save()
        messages.success(request, ' Data added Successfully.')

        if created:
           return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'bookingengine/settings/contact-info.html', {'contact': contact})


def color_palette(request):
    
    try:
        color = ColorPalettes.objects.get(user_id=request.user.id)
        created = False
    except ColorPalettes.DoesNotExist:
        color = ColorPalettes(user_id=request.user.id)
        print(color)
        created = True

    if request.method == 'POST':
        color.top_background_colour = request.POST.get('top_background_color')
        color.top_font_colour = request.POST.get('top_font_color')
        color.footer_background_colour = request.POST.get('footer_background_color')
        color.footer_font_colour = request.POST.get('footer_font_color')
        color.user_id = request.user.id
        color.status = 1
        color.save()
        messages.success(request, ' Data added Successfully.')

        if created:
           return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'bookingengine/settings/color-palette.html', {'color': color})


# Widget code start
@login_required(login_url='/booking-engine/')
def widget_insert(request):  
    if request.method == "POST":
        widget=FooterWidgets()
        widget.title=request.POST.get('title')   
        widget.description=request.POST.get('description') 
        widget.user_id=request.user.id
        widget.status=request.POST.get('status')
        widget.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/widgets')   

@login_required(login_url='/booking-engine/')
def widget_add(request):
    return render (request,"bookingengine/widgets/widget-add.html")     
       
@login_required(login_url='/booking-engine/')
def widgets(request):  
    widget = FooterWidgets.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/widgets/widgets.html",{'widget':widget})  

@login_required(login_url='/booking-engine/')
def widget_edit(request, id):  
    widget = FooterWidgets.objects.get(id=id)  
    return render(request,'bookingengine/widgets/widget-edit.html', {'widget':widget})  

@login_required(login_url='/booking-engine/')
def widget_update(request, id):  
    if request.method == "POST":
        widget=FooterWidgets.objects.get(id=id)
        widget.title=request.POST.get('title')   
        widget.description=request.POST.get('description') 
        widget.status=request.POST.get('status')
        widget.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/widgets')  

@login_required(login_url='/booking-engine/')
def widget_destroy(request, id):  
    widget = FooterWidgets.objects.get(id=id)  
    widget.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/widgets') 

# Widget Code end

def term_condition(request):
    
    try:
        tc = TermCondition.objects.get(user_id=request.user.id)
        created = False
    except TermCondition.DoesNotExist:
        tc = TermCondition(user_id=request.user.id)
        created = True

    if request.method == 'POST':
        tc.title = request.POST.get('title')
        tc.description = request.POST.get('description')
        tc.user_id = request.user.id
        tc.status = request.POST.get('status')
        tc.save()
        messages.success(request, ' Data added Successfully.')

        if created:
           return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'bookingengine/settings/term-condition.html', {'tc': tc})

#ExtraServices code start

@login_required(login_url='/booking-engine/')
def extra_service_insert(request):  
    if request.method == "POST":
        service=ExtraService()
        service.title=request.POST.get('title')
        service.price=request.POST.get('price')   
        service.description=request.POST.get('description') 
        service.user_id=request.user.id
        service.status=request.POST.get('status')
        service.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/booking-engine/extra-services')   

@login_required(login_url='/booking-engine/')
def extra_service_add(request):
    return render (request,"bookingengine/additional-details/extra-service-add.html")     
       
@login_required(login_url='/booking-engine/')
def extra_services(request):  
    service = ExtraService.objects.filter(user_id=request.user.id)
    return render(request,"bookingengine/additional-details/extra-services.html",{'service':service})  

@login_required(login_url='/booking-engine/')
def extra_service_edit(request, id):  
    service = ExtraService.objects.get(id=id)  
    return render(request,'bookingengine/additional-details/extra-service-edit.html', {'service':service})  

@login_required(login_url='/booking-engine/')
def extra_service_update(request, id):  
    if request.method == "POST":
        service=ExtraService.objects.get(id=id)
        service.title=request.POST.get('title')
        service.price=request.POST.get('price')   
        service.description=request.POST.get('description') 
        service.user_id=request.user.id
        service.status=request.POST.get('status')
        service.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/booking-engine/extra-services')  

@login_required(login_url='/booking-engine/')
def extra_service_destroy(request, id):  
    service = ExtraService.objects.get(id=id)  
    service.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect('/booking-engine/extra-services') 

#ExtraServices code end


def booking_information(request):
    if request.method == "POST":
        booking=BookingInformation()
        booking.honorific=request.POST.get('honorific')
        booking.first_name=request.POST.get('first_name')
        booking.last_name=request.POST.get('last_name')
        booking.email=request.POST.get('email')
        booking.phone=request.POST.get('phone')
        booking.address=request.POST.get('address')
        booking.zip_code=request.POST.get('zip_code')
        booking.city=request.POST.get('city')
        booking.state=request.POST.get('state')
        booking.country=request.POST.get('country')
        booking.notes=request.POST.get('notes')
        booking.card_holder_name=request.POST.get('card_holder_name')
        booking.credit_card_number=request.POST.get('credit_card_number')
        booking.expiry_month=request.POST.get('expiry_month')
        booking.expiry_year=request.POST.get('expiry_year')
        booking.cvv=request.POST.get('cvv')
        booking.check_in=request.POST.get('check_in')
        booking.check_out=request.POST.get('check_out')
        booking.room=request.POST.get('room')
        booking.room_id=request.POST.get('room_id')
        booking.adult=request.POST.get('adult')
        booking.child=request.POST.get('child')
        booking.no_of_guest=request.POST.get('no_of_guest')
        booking.no_of_nights=request.POST.get('no_of_nights')
        booking.price=request.POST.get('price')
        booking.tax=request.POST.get('tax')
        booking.total_price=request.POST.get('total_price')
        booking.term_condition=request.POST.get('term_condition')
        booking.user_id=request.user.id
        booking.extra_services=request.POST.getlist('name[]')
        booking.save()
        return redirect('/booking-engine')


