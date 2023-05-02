import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rentals.forms import CreateUserForm, InvoiceForm, InvoiceItemFormset
from rentals.models import  Activity, BasicRates, CustomServices, EarlyBirdDiscount, ExtraServices, HouseRules, LongStayDiscount, OtherRooms, Amenities, AmenitiesType, Attributes, Bed, Bookings, Category, Channel, CompanyProfile, Country, Discount, DiscountType,Currency, Invoice, InvoiceItem, Partner, Policy, PropertyRole, Rate, Ratetype, Rental, RentalAmenities, RentalBasic, RentalCleaning, RentalDeposit, RentalInstruction, RentalLocation, RentalOtherRooms, RentalPolicy, RentalTax, RentalsGallery, Rentaltype, Room, Roomtype, SeasonalRates, Services, Subscription, Tax, Taxtype, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/super/dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user)

                return redirect('/super/')
            else:
                messages.success(request, 'Invalid credentials.')    
            

        context = {'form':form}
        return render(request, 'super/authentication/register.html', context)

def auth_view(request):
    if request.user.is_authenticated:
        return redirect('/super/dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password =request.POST['password']
            user = authenticate(username=username, password=password)
                    
            if user is not None:
                    login(request, user)
                    return redirect('/super/dashboard')
            else:
                messages.error(request, "Invalid email or password")
                return redirect('/super/dashboard')
    
    return render(request,'super/authentication/login.html')  

def logoutUser(request):
    logout(request)
    return redirect('/super/login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/change-password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'super/change-password.html', {
        'form': form
    })    

# Dashboard Code Start
@login_required(login_url='/super/')
def index(request):
    return render(request,'super/dashboard/index.html')

# Dashboard Code End

# User Management Code Start 

@login_required(login_url='/super/')
def users(request):
   User = get_user_model()
   users = User.objects.all()
   return render(request, 'super/users/users.html', {'users': users})

@login_required(login_url='/super/')
def user_insert(request):
    if request.method == 'POST':
        User = get_user_model()
        users = User()
        users.first_name = request.POST.get('first_name')
        users.last_name = request.POST.get('last_name')
        users.username = request.POST.get('username')
        users.email = request.POST.get('email')
        users.is_superuser=request.POST.get('is_superuser')
        users.is_staff=request.POST.get('is_staff')
        users.password = request.POST.get('password')
        users.is_active = request.POST.get('is_active')
        users.save()
        messages.success(request, ' Row added Successfully.')

        LastInsertId = (User.objects.last()).id
        LastRow = User.objects.get(id=LastInsertId)
       
        if LastRow.is_staff==0 and LastRow.is_superuser== 0:
        
            UserProfiles = UserProfile() 
            UserProfiles.first_name = LastRow.first_name
            UserProfiles.last_name = LastRow.last_name
            UserProfiles.phone = 'NA'
            UserProfiles.address = 'NA'
            UserProfiles.city= 'NA'
            UserProfiles.state='NA'
            UserProfiles.country = 'NA'
            UserProfiles.postal_code = 'NA'
            UserProfiles.property_phone_number = 'NA'
            UserProfiles.tollfree = 'NA'
            UserProfiles.website = 'NA'
            UserProfiles.property_logo = ''
            UserProfiles.status = '1'
            UserProfiles.user_id =  LastRow.id           
            UserProfiles.save()
        
        
       
   

    return redirect('/super/users')

@login_required(login_url='/super/')
def user_add(request):
    return render(request,'super/users/user-add.html')        

@login_required(login_url='/super/')
def user_edit(request,id):
   User = get_user_model()
   users = User.objects.get(id=id)
   return render(request, 'super/users/user-edit.html', {'users': users})

@login_required(login_url='/super/')
def user_update(request, id):  
    
    User = get_user_model()
    users = User.objects.get(id=id) 
    if request.method == 'POST':
    
        users.first_name = request.POST.get('first_name')
        users.last_name = request.POST.get('last_name')
        users.username = request.POST.get('username')
        users.email = request.POST.get('email')
        users.is_superuser=request.POST.get('is_superuser')
        users.is_staff=request.POST.get('is_staff')
        users.password = request.POST.get('password')
        users.is_active = request.POST.get('is_active')
        users.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/users')
    return render(request, 'super/users/usertype-edit.html"', {'users': users}) 
      
          
@login_required(login_url='/super/')       
def user_delete(request, id):  
    User = get_user_model()
    users = User.objects.get(id=id)
    users.delete()
    messages.success(request, ' Row deleted Successfully.')
    return redirect("/super/users")     


@login_required(login_url='/super/')
def user_profile(request):
    users= UserProfile.objects.all()
  
    context={
        'users': users,
       

    }
    return render(request, "super/users/user-profile.html",context)

@login_required(login_url='/super/')
def user_profile_add(request):
    return render(request, "super/users/user-profile-add.html")

@login_required(login_url='/super/')
def user_profile_edit(request,id):
    users = UserProfile.objects.get(id=id)
    return render(request, "super/users/user-profile-edit.html", {'users': users})

@login_required(login_url='/super/')    
def user_profile_update(request,id):
    users = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        users.first_name =  request.POST.get('first_name')
        users.last_name =  request.POST.get('last_name')
        users.phone =  request.POST.get('phone')
        users.address =  request.POST.get('address')
        users.city=  request.POST.get('city')
        users.state= request.POST.get('state')
        users.country =  request.POST.get('country')
        users.postal_code =  request.POST.get('postal_code')
        users.property_phone_number =  request.POST.get('property_phone_number')
        users.tollfree =  request.POST.get('tollfree')
        users.website =  request.POST.get('website')
        users.property_logo =  request.FILES.get('property_logo')
        users.status =  request.POST.get('status')           
        users.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect ('/super//user-profile')

    return render(request, "super/users/user-profile-edit.html", {'users': users})

@login_required(login_url='/super/')
def user_profile_delete(request, id):  
    users = UserProfile.objects.get(id=id)
    users.delete()
    messages.success(request, ' Row deleted Successfully.')
    return redirect("/super/user-profile")         

@login_required(login_url='/super/')
def user_indivisual_profile(request, id):
    user_profile = UserProfile.objects.get(id=id)
    user =user_profile.user
    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return redirect('/super/user-profile')

    
    property_logo=user_profile.property_logo
    User = get_user_model()
    user_indivisual = User.objects.get(id=user_profile.user_id)
    users={
        'user_profile':user_profile,
        'user_indivisual':user_indivisual,
        'property_logo':property_logo,
        'user': user
    }
    return render(request, "super/users/user-indivisual-profile.html",users)

@login_required(login_url='/super/')
def user_indivisual_profile_update(request, id):
    user_profile = UserProfile.objects.get(id=id)
    User = get_user_model()
    user_indivisual = User.objects.get(id=user_profile.user_id)
    if request.method == 'POST':
        user_indivisual.set_password(request.POST.get('password'))
        user_indivisual.save()
        messages.success(request, 'Password changed successfully.')
        return redirect (request.META['HTTP_REFERER']) 

# User Management Code End


# Channels Code Start

@login_required(login_url='/super/')
def channel_insert(request):
    if request.method == "POST": 
        employee=Channel()
        employee.channel_title=request.POST.get('channel_title')
        employee.channel_image=request.FILES.get('channel_image')
        employee.channel_description=request.POST.get('channel_description')
        employee.status=request.POST.get('status')
        employee.save()
        messages.success(request, ' Row added Successfully.')
    return redirect ("/super/channels")

    

@login_required(login_url='/super/')     
def channel_add(request):
    return render(request,"super/channels/channel-add.html")  

@login_required(login_url='/super/')
def channels(request):  
    channels = Channel.objects.all()  
    return render(request,"super/channels/channels.html",{'employees':channels})  

@login_required(login_url='/super/')
def channel_edit(request, id):  
    channel= Channel.objects.get(id=id)  
    return render(request,'super/channels/channel-edit.html', {'employee':channel})  

@login_required(login_url='/super/')
def channel_update(request, id):    
    if request.method == "POST": 
        employee= Channel.objects.get(id=id)
        employee.channel_title=request.POST.get('channel_title')
        if 'channel_image' in request.FILES:
           employee.channel_image = request.FILES['channel_image']
        employee.channel_description=request.POST.get('channel_description')
        employee.status=request.POST.get('status')
        employee.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/channels')
   
    return render(request, 'super/channels/channel-edit.html', {'employee': employee})  

@login_required(login_url='/super/')
def channel_destroy(request, id):  
    channel = Channel.objects.get(id=id)  
    channel.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/channels") 

# Channel Code End   

# Amenities Type code start
@login_required(login_url='/super/')  
def amenities_type(request):
    amenitiestype=AmenitiesType.objects.all() 
    return render(request, 'super/amenities/amenities-type.html', {'amenitiestype': amenitiestype})

@login_required(login_url='/super/')  
def amenities_type_insert(request):
    if request.method == "POST":
        amenitiestype=AmenitiesType()
        amenitiestype.title=request.POST.get('title')
        amenitiestype.status=request.POST.get('status')
        amenitiestype.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/amenities-type')    


@login_required(login_url='/super/')  
def amenities_type_add(request):
    return render(request, 'super/amenities/amenities-type-add.html')

@login_required(login_url='/super/')  
def amenities_type_edit(request,id):
    amenitiestype=AmenitiesType.objects.get(id=id) 
    return render(request, 'super/amenities/amenities-type-edit.html', {'amenitiestype': amenitiestype})

@login_required(login_url='/super/')  
def amenities_type_update(request,id):
    if request.method == "POST":
        amenitiestype=AmenitiesType.objects.get(id=id)
        amenitiestype.title=request.POST.get('title')
        amenitiestype.status=request.POST.get('status')
        amenitiestype.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/amenities-type') 
    return render(request, 'super/amenities/amenities-type-edit.html', {'amenitiestype': amenitiestype})

@login_required(login_url='/super/')  
def amenities_type_destroy(request, id):  
    amenitiestype = AmenitiesType.objects.get(id=id)  
    amenitiestype.delete()
    messages.success(request, ' Row deleted Successfully.')    
    return redirect("/super/amenities-type")   


#Amenities Type code end 

# Amenities code start

@login_required(login_url='/super/')
def amenities_insert(request): 
    if request.method == "POST":
        amenities=Amenities()
        amenities.amenities_type_id=request.POST.get('amenities_type')
        amenities.title=request.POST.get('title')  
        amenities.status=request.POST.get('status')
        amenities.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/amenities')
       

   

@login_required(login_url='/super/')
def amenities_add(request):
    amenitiestype=AmenitiesType.objects.all()
    return render (request,"super/amenities/amenities-add.html",{'amenitiestype':amenitiestype})     
       
@login_required(login_url='/super/')
def amenities(request):  
    amenities = Amenities.objects.all()  
    return render(request,"super/amenities/amenities.html",{'amenities':amenities})  

@login_required(login_url='/super/')
def amenities_edit(request, id):  
    amenities = Amenities.objects.get(id=id)
    amenitiestype=AmenitiesType.objects.all()
    context={
        'amenities':amenities,
        'amenitiestype':amenitiestype

    } 
    return render(request,'super/amenities/amenities-edit.html',context)  

@login_required(login_url='/super/')
def amenities_update(request, id):  
    amenities = Amenities.objects.get(id=id) 
    if request.method == "POST":
        amenities.amenities_type_id=request.POST.get('amenities_type')
        amenities.title=request.POST.get('title')  
        amenities.status=request.POST.get('status')
        amenities.save()
        messages.success(request, ' Row updated Successfully.')

    return redirect('/super/amenities')  
   

@login_required(login_url='/super/')
def amenities_destroy(request, id):  
    amenities = Amenities.objects.get(id=id)  
    amenities.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/amenities")

# Amenities code end      

# Activity code start

@login_required(login_url='/super/')
def activity(request):  
    activity = Activity.objects.all()  
    return render(request,"super/amenities/activity.html",{'activity':activity})  

@login_required(login_url='/super/')
def activity_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/amenities/activity-add.html',{'users':User})

@login_required(login_url='/super/')
def activity_insert(request):
    if request.method == "POST":
        activity=Activity()
        activity.name=request.POST.get('name')
        activity.distance=request.POST.get('distance')
        activity.description=request.POST.get('description')
        activity.user_id=request.POST.get('user_id')
        activity.status=request.POST.get('status')
        activity.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/activity')    

@login_required(login_url='/super/')
def activity_edit(request,id):  
    activity = Activity.objects.get(id=id)  
    return render(request,'super/amenities/activity-edit.html',{'activity':activity})  

@login_required(login_url='/super/')
def activity_update(request,id):
    activity = Activity.objects.get(id=id)
    if request.method == "POST":
        activity.name=request.POST.get('name')
        activity.distance=request.POST.get('distance')
        activity.description=request.POST.get('description')
        activity.status=request.POST.get('status')
        activity.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/activity')   

      
    
    return render(request, 'super/amenities/activity-edit.html',{'activity':activity})  

@login_required(login_url='/super/')
def activity_destroy(request, id):  
    activity = Activity.objects.get(id=id)  
    activity.delete() 
    messages.success(request, ' Row deleted Successfully.')

    return redirect("/super/activity")   


# Activity code end

# Room-Type Code Start

@login_required(login_url='/super/')
def rental_type_insert(request):
    if request.method == "POST": 
        rentaltype=Rentaltype()
        rentaltype.room_type_name=request.POST.get('room_type_name')
        rentaltype.noof_beds=request.POST.get('noof_beds')
        rentaltype.max_occupancy=request.POST.get('max_occupancy')
        rentaltype.noof_rooms=request.POST.get('noof_rooms')
        rentaltype.picture=request.FILES.get('picture')
        rentaltype.rental_description=request.POST.get('rental_description')
        rentaltype.user_id=request.POST.get('user_id')
        rentaltype.status=request.POST.get('status')
        rentaltype.save()
        messages.success(request, ' Row added Successfully.')
    return redirect ('/super/rental-type')

    

@login_required(login_url='/super/')     
def rental_type_add(request):
    User = get_user_model().objects.all()
    return render(request,"super/rentals/rental-type-add.html",{'users':User})  

@login_required(login_url='/super/')
def rental_type(request):  
    rentaltype = Rentaltype.objects.all()  
    return render(request,"super/rentals/rental-type.html",{'rentaltype':rentaltype})  

@login_required(login_url='/super/')
def rental_type_edit(request, id):  
    rentaltype= Rentaltype.objects.get(id=id)  
    return render(request,'super/rentals/rental-type-edit.html', {'rentaltype':rentaltype})  

@login_required(login_url='/super/')
def rental_type_update(request, id):    
    if request.method == "POST": 
        rentaltype= Rentaltype.objects.get(id=id)
        rentaltype.room_type_name=request.POST.get('room_type_name')
        rentaltype.noof_beds=request.POST.get('noof_beds')
        rentaltype.max_occupancy=request.POST.get('max_occupancy')
        rentaltype.noof_rooms=request.POST.get('noof_rooms')
        if 'picture' in request.FILES:
             rentaltype.picture=request.FILES.get('picture')
        rentaltype.rental_description=request.POST.get('rental_description')
        rentaltype.status=request.POST.get('status')
        rentaltype.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/rental-type')
   
    return render(request, 'super/rentals/rental-type-edit.html', {'rentaltype': rentaltype})  

@login_required(login_url='/super/')
def rental_type_destroy(request, id):  
    rentaltype = Rentaltype.objects.get(id=id)  
    rentaltype.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/rental-type") 

# Room Type Code End    

# Tax Type code start
@login_required(login_url='/super/')  
def tax_type(request):
    taxtype=Taxtype.objects.all() 
    return render(request, 'super/tax/tax-type.html', {'taxtype': taxtype})

@login_required(login_url='/super/')  
def tax_type_insert(request):
    if request.method == "POST":
        taxtype=Taxtype()
        taxtype.taxtype_name=request.POST.get('taxtype_name')
        taxtype.user_id=request.POST.get('user_id')
        taxtype.status=request.POST.get('status')
        taxtype.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/tax-type')    


@login_required(login_url='/super/')  
def tax_type_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/tax/tax-type-add.html',{'users':User})

@login_required(login_url='/super/')  
def tax_type_edit(request,id):
    taxtype=Taxtype.objects.get(id=id) 
    return render(request, 'super/tax/tax-type-edit.html', {'taxtype': taxtype})

@login_required(login_url='/super/')  
def tax_type_update(request,id):
    taxtype=Taxtype.objects.get(id=id)
    if request.method == "POST":
        taxtype.taxtype_name=request.POST.get('taxtype_name')
        taxtype.status=request.POST.get('status')
        taxtype.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/tax-type') 
    return render(request, 'super/tax/tax-type-edit.html', {'taxtype': taxtype})

@login_required(login_url='/super/')  
def tax_type_destroy(request, id):  
    taxtype = Taxtype.objects.get(id=id)  
    taxtype.delete()
    messages.success(request, ' Row deleted Successfully.')    
    return redirect("/super/tax-type")   


#Tax Type code end

# Tax code start
@login_required(login_url='/super/')  
def tax_add(request):
    taxtype=Taxtype.objects.all()
    User = get_user_model().objects.all()
    context={
        'taxtype':taxtype,
        'users':User
    }
    return render(request, 'super/tax/tax-add.html',context)

@login_required(login_url='/super/')  
def tax_insert(request):  
    if request.method == "POST":
        tax=Tax()
        tax.tax_type_id=request.POST.get('tax_type')
        tax.tax_name=request.POST.get('tax_name')
        tax.tax_percentage=request.POST.get('tax_percentage')
        tax.user_id=request.POST.get('user_id')
        tax.status=request.POST.get('status')
        tax.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/super/tax')    

@login_required(login_url='/super/')        
def tax(request):  
    tax= Tax.objects.all()  
    return render(request,"super/tax/tax.html",{'tax':tax})  

@login_required(login_url='/super/')  
def tax_edit(request, id):  
    tax = Tax.objects.get(id=id) 
    taxtype=Taxtype.objects.all()
    context={
        'tax':tax,
        'taxtype':taxtype
    }
    return render(request,'super/tax/tax-edit.html',context)  

@login_required(login_url='/super/')  
def tax_update(request, id):  
    tax = Tax.objects.get(id=id)
    taxtype=Taxtype.objects.all()
    if request.method == "POST":
        tax.tax_type_id=request.POST.get('tax_type')
        tax.tax_name=request.POST.get('tax_name')
        tax.tax_percentage=request.POST.get('tax_percentage')
        tax.status=request.POST.get('status')
        tax.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/super/tax') 

    context={
        'tax': tax,
        'taxtype':taxtype


    }
       
    return render(request, 'super/tax/tax-edit.html',context)  

@login_required(login_url='/super/')  
def tax_destroy(request, id):  
    tax = Tax.objects.get(id=id)  
    tax.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/super/tax")   

# Tax code end

# Policy Code Start

@login_required(login_url='/super/')  
def policy(request):
    policy=Policy.objects.all()
    return render(request, 'super/policy/policy.html',{'policy':policy})

@login_required(login_url='/super/')  
def policy_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/policy/policy-add.html',{'users':User}) 

@login_required(login_url='/super/')  
def policy_insert(request):
    if request.method == "POST":
        policy=Policy()
        policy.policy_number=request.POST.get('policy_number')
        policy.policy_name=request.POST.get('policy_name')
        policy.policy_type=request.POST.get('policy_type')
        policy.description=request.POST.get('description')
        policy.user_id=request.POST.get('user_id')
        policy.status=request.POST.get('status')
        policy.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/policy')
       
@login_required(login_url='/super/')  
def policy_edit(request,id):
    policy=Policy.objects.get(id=id)
    return render(request, 'super/policy/policy-edit.html',{'policy':policy})       

@login_required(login_url='/super/')  
def policy_update(request,id):
    policy=Policy.objects.get(id=id)
    if request.method == "POST":  
        policy.policy_number=request.POST.get('policy_number')
        policy.policy_name=request.POST.get('policy_name')
        policy.policy_type=request.POST.get('policy_type')
        policy.description=request.POST.get('description')
        policy.status=request.POST.get('status')
        policy.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/policy')
    return render(request, 'super/policy/policy-edit.html',{'policy':policy})

@login_required(login_url='/super/')  
def policy_destroy(request,id): 
    policy = Policy.objects.get(id=id)  
    policy.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/policy")  


# Rate Type code start

@login_required(login_url='/super/')  
def rate_type(request):
    ratetype=Ratetype.objects.all() 
    return render(request, 'super/rates/rate-type.html', {'ratetype': ratetype})

@login_required(login_url='/super/')  
def rate_type_insert(request):
    if request.method == "POST":
        ratetype=Ratetype()
        ratetype.ratetype_name=request.POST.get('ratetype_name')
        ratetype.user_id=request.POST.get('user_id')
        ratetype.status=request.POST.get('status')
        ratetype.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/rate-type')    

@login_required(login_url='/super/')  
def rate_type_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/rates/rate-type-add.html',{'users':User})

@login_required(login_url='/super/')  
def rate_type_edit(request,id):
    ratetype=Ratetype.objects.get(id=id) 
    return render(request, 'super/rates/rate-type-edit.html', {'ratetype': ratetype})

@login_required(login_url='/super/')  
def rate_type_update(request,id):
    ratetype=Ratetype.objects.get(id=id)
    if request.method == "POST":
        ratetype.ratetype_name=request.POST.get('ratetype_name')
        ratetype.status=request.POST.get('status')
        ratetype.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/rate-type') 
    return render(request,' super/rates/rate-type-edit.html', {'ratetype': ratetype})

@login_required(login_url='/super/')  
def rate_type_destroy(request, id):  
    ratetype = Ratetype.objects.get(id=id)  
    ratetype.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/rate-type")   

#Rate Type code end

#Rate code start

@login_required(login_url='/super/')  
def rate(request):
    rate=Rate.objects.all() 
    return render(request, 'super/rates/rate.html' ,{'rate': rate})

@login_required(login_url='/super/')  
def rate_add(request):
    ratetype=Ratetype.objects.all()
    users = get_user_model().objects.all() 
    context={
        'ratetype':ratetype,
        'users':users
    }
    return render(request, 'super/rates/rate-add.html',context)

@login_required(login_url='/super/')  
def rate_insert(request):
    if request.method == "POST":
        rate=Rate()
        rate.rate_type_id=request.POST.get('rate_type')
        rate.rate_name=request.POST.get('rate_name')
        rate.included_occupants=request.POST.get('included_occupants')
        rate.extra_adult_charge=request.POST.get('extra_adult_charge')
        rate.extra_children_charge=request.POST.get('extra_children_charge')
        rate.weekend_surcharge=request.POST.get('weekend_surcharge')
        rate.day_surcharge=request.POST.getlist('day_surcharge[]')
        rate.disable_rates=request.POST.get('disable_rates')
        rate.description=request.POST.get('description')
        rate.status=request.POST.get('status')
        rate.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/rate')

@login_required(login_url='/super/')  
def rate_edit(request,id):
    rate=Rate.objects.get(id=id) 
    ratetype=Ratetype.objects.all() 
    context = {
        'rate':rate,
        'ratetype':ratetype
    }
    return render(request, 'super/rates/rate-edit.html',context)

@login_required(login_url='/super/')  
def rate_update(request,id):
    rate=Rate.objects.get(id=id)
    if request.method == "POST":
       rate.rate_type_id=request.POST.get('rate_type')
       rate.rate_name=request.POST.get('rate_name')
       rate.included_occupants=request.POST.get('included_occupants')
       rate.extra_adult_charge=request.POST.get('extra_adult_charge')
       rate.extra_children_charge=request.POST.get('extra_children_charge')
       rate.weekend_surcharge=request.POST.get('weekend_surcharge')
       rate.day_surcharge=request.POST.getlist('day_surcharge[]')
       rate.disable_rates=request.POST.get('disable_rates')
       rate.description=request.POST.get('description')
       rate.status=request.POST.get('status')
       print(rate.day_surcharge)
       rate.save()
       messages.success(request, ' Row edited Successfully.')
       return redirect('/super/rate')
        
    return render(request,' super/rates/rate-edit.html', {'rate': rate})

@login_required(login_url='/super/')  
def rate_destroy(request, id):  
    rate = Rate.objects.get(id=id)  
    rate.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/rate")       

#Rate code end

# Booking Code start

@login_required(login_url='/super/')  
def booking(request):
    bookings=Bookings.objects.all()
    return render (request,'super/bookings/bookings.html', {'bookings': bookings})

@login_required(login_url='/super/')  
def booking_edit(request, id):
    bookings=Bookings.objects.get(id=id) 
    channels=Channel.objects.all()
    context={
        'bookings':bookings,
        'channels':channels
    }
    return render (request,'super/bookings/booking-edit.html',context)    

@login_required(login_url='/super/')  
def booking_update(request ,id):
    bookings=Bookings.objects.get(id=id) 
    channels=Channel.objects.all()
    if request.method == "POST":
        bookings.rental=request.POST.get('rental')
        bookings.channel_id=request.POST.get('channel')
        bookings.booking_type=request.POST.get('booking_type')
        bookings.first_name =  request.POST.get('first_name')
        bookings.last_name =  request.POST.get('last_name')
        bookings.phone =  request.POST.get('phone')
        bookings.address =  request.POST.get('address')
        bookings.city=  request.POST.get('city')
        bookings.state= request.POST.get('state')
        bookings.country =  request.POST.get('country')
        bookings.postal_code =  request.POST.get('postal_code')
        bookings.check_in=request.POST.get('check_in')
        bookings.check_out=request.POST.get('check_out')
        bookings.status=request.POST.get('status')
        bookings.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/bookings') 
        
    context={
        'bookings':bookings,
        'channels':channels
    }    
    return render(request, 'super/bookings/booking-edit.html',context)     

@login_required(login_url='/super/')  
def booking_view(request,id):
    bookings=Bookings.objects.get(id=id)
    return render (request,'super/bookings/bookings_view.html', {'bookings': bookings})


# Discount Type code start

@login_required(login_url='/super/')  
def discount_type(request):
    discounttype=DiscountType.objects.all() 
    return render(request, 'super/discounts/discount-type.html', {'discounttype': discounttype})

@login_required(login_url='/super/')  
def discount_type_insert(request):
    if request.method == "POST":
        discounttype=DiscountType()
        discounttype.discounttype_name=request.POST.get('discounttype_name')
        discounttype.user_id=request.POST.get('user_id')
        discounttype.status=request.POST.get('status')
        discounttype.save()
        messages.success(request, ' Row added Successfully.')  
        return redirect('/super/discount-type')    

@login_required(login_url='/super/')  
def discount_type_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/discounts/discount-type-add.html',{'users':User})

@login_required(login_url='/super/')  
def discount_type_edit(request,id):
    discounttype=DiscountType.objects.get(id=id) 
    return render(request, 'super/discounts/discount-type-edit.html', {'discounttype': discounttype})

@login_required(login_url='/super/')  
def discount_type_update(request,id):
    discounttype=DiscountType.objects.get(id=id)
    if request.method == "POST":
        discounttype.discounttype_name=request.POST.get('discounttype_name')
        discounttype.status=request.POST.get('status')
        discounttype.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect('/super/discount-type') 
    return render(request,' super/discounts/discount-type-edit.html', {'discounttype': discounttype})

@login_required(login_url='/super/')  
def discount_type_destroy(request, id):  
    discounttype = DiscountType.objects.get(id=id)  
    discounttype.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/discount-type")   

#Discount Type code end

#Discount code start

@login_required(login_url='/super/')  
def discount(request):
    discount=Discount.objects.all() 
    return render(request, 'super/discounts/discounts.html' ,{'discount': discount})

@login_required(login_url='/super/')  
def discount_add(request):
    discounttype=DiscountType.objects.all() 
    User = get_user_model().objects.all()
    context={
        'discounttype':discounttype,
        'users':User
    }
    return render(request, 'super/discounts/discount-add.html',context)

@login_required(login_url='/super/')  
def discount_insert(request):
    if request.method == "POST":
        discount=Discount()
        discount.discounts_name=request.POST.get('discounts_name')
        discount.discount_type_id=request.POST.get('discount_type')
        discount.discounts_amount=request.POST.get('discounts_amount')
        discount.status=request.POST.get('status')
        discount.user_id=request.POST.get('user_id')
        discount.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/discounts')

@login_required(login_url='/super/')  
def discount_edit(request,id):
    discount=Discount.objects.get(id=id) 
    discounttype=DiscountType.objects.all() 
    context = {
        'discount':discount,
        'discounttype':discounttype
    }
    return render(request, 'super/discounts/discount-edit.html',context)

@login_required(login_url='/super/')  
def discount_update(request,id):
    discount=Discount.objects.get(id=id)
    if request.method == "POST":
        discount.discounts_name=request.POST.get('discounts_name')
        discount.discount_type_id=request.POST.get('discount_type')
        discount.discounts_amount=request.POST.get('discounts_amount')
        discount.status=request.POST.get('status')
        discount.save()
        messages.success(request, ' Row edited Successfully.')
        return redirect('/super/discounts')
        
    return render(request,' super/discounts/discount-edit.html', {'discount': discount})

@login_required(login_url='/super/')  
def discount_destroy(request, id):  
    discount = Discount.objects.get(id=id)  
    discount.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/discounts")       

# Discount code end

# Currency code start

@login_required(login_url='/super/')  
def currency(request):
    currency=Currency.objects.all() 
    return render(request, 'super/discounts/currency.html' ,{'currency': currency})

@login_required(login_url='/super/')  
def currency_add(request):
    User = get_user_model().objects.all()
    return render(request, 'super/discounts/currency-add.html',{'users':User})

@login_required(login_url='/super/')  
def currency_insert(request):
    if request.method == "POST":
        currency=Currency()
        currency.title=request.POST.get('title')
        currency.code=request.POST.get('code')
        currency.symbol=request.POST.get('symbol')
        currency.decimal_place=request.POST.get('decimal_place')
        currency.currency_value=request.POST.get('currency_value')
        currency.status=request.POST.get('status')

        currency.save()
        messages.success(request, ' Row added Successfully.')
        return redirect('/super/currency')

@login_required(login_url='/super/')  
def currency_edit(request,id):
    currency=Currency.objects.get(id=id)
    context = {
        'currency':currency
    }
    return render(request, 'super/discounts/currency-edit.html',context)

@login_required(login_url='/super/')  
def currency_update(request,id):
    currency=Currency.objects.get(id=id)
    if request.method == "POST":
        currency.title=request.POST.get('title')
        currency.code=request.POST.get('code')
        currency.symbol=request.POST.get('symbol')
        currency.decimal_place=request.get('decimal_place')
        currency.currency_value=request.get('currency_value')
        currency.status=request.POST.get('status')
        currency.save()
        messages.success(request, ' Row edited Successfully.')
        return redirect('/super/currency')
        
    return render(request,' super/discounts/currency-edit.html', {'currency': currency})

@login_required(login_url='/super/')  
def currency_destroy(request, id):  
    currency = Currency.objects.get(id=id)  
    currency.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/currency")       

# Currency code end

# Rental Code start
@login_required(login_url='/super/')  
def rental_insert(request):
    if request.method == "POST": 
        rental=Rental()
        rental.rental_name=request.POST.get('rental_name')
        rental.cover_image=request.FILES.get('cover_image')
        rental.rental_short_description=request.POST.get('rental_short_description')
        rental.rental_description=request.POST.get('rental_description')
        rental.user_id=request.POST.get('user_id')
        rental.save()
        LastInsertId = (Rental.objects.last()).id
        LastRow = Rental.objects.get(id=LastInsertId)

        rentalbasic=RentalBasic()
        rentalbasic.rental_type=""
        rentalbasic.rental_basis=""
        rentalbasic.floorspace=""
        rentalbasic.floorspace_units=""
        rentalbasic.grounds=""
        rentalbasic.grounds_units=""
        rentalbasic.floors_building=""
        rentalbasic.entrance=""
        rentalbasic.rental_licence=""
        rentalbasic.user_id=rental.user_id
        rentalbasic.rental_id=LastRow.id
        rentalbasic.save()

        location=RentalLocation()
        location.country=""
        location.address=""
        location.apartment=""
        location.city=""
        location.state=""
        location.postal=""
        location.user_id=request.user.id
        location.rental_id=LastRow.id
        location.save()

        rentalamenities=RentalAmenities()
        rentalamenities.amenities=""
        rentalamenities.user_id=request.user.id
        rentalamenities.rental_id=LastRow.id
        rentalamenities.save()

        longstaydiscount=LongStayDiscount()
        longstaydiscount.seven_nights=""
        longstaydiscount.fourteen_nights=""
        longstaydiscount.twenty_one_nights=""
        longstaydiscount.twenty_eight_nights=""
        longstaydiscount.user_id=request.user.id
        longstaydiscount.rental_id=LastRow.id
        longstaydiscount.save()

        earlybirddiscount=EarlyBirdDiscount()
        earlybirddiscount.booking_less=""
        earlybirddiscount.booking_less_discount=""
        earlybirddiscount.booking_more=""
        earlybirddiscount.booking_more_discount=""
        earlybirddiscount.user_id=request.user.id
        earlybirddiscount.rental_id=LastRow.id
        earlybirddiscount.save()

        houserules=HouseRules()
        houserules.for_kid=""
        houserules.wheelchair_access=""
        houserules.parties_allowed=""
        houserules.smoking_allowed=""
        houserules.pets=""
        houserules.house_rules=""
        houserules.user_id=request.user.id
        houserules.rental_id=LastRow.id
        houserules.save()

        rentalpolicy=RentalPolicy()
        rentalpolicy.name=""
        rentalpolicy.description=""
        rentalpolicy.user_id=request.user.id
        rentalpolicy.rental_id=LastRow.id
        rentalpolicy.save()

        rentalinstruction=RentalInstruction()
        rentalinstruction.checkin_instruction=""
        rentalinstruction.checkout_instruction=""
        rentalinstruction.checkin_contact=""
        rentalinstruction.key_collection=""
        rentalinstruction.telephone_country=""
        rentalinstruction.telephone_number=""
        rentalinstruction.instructions=""
        rentalinstruction.attach_instruction=""
        rentalinstruction.checkin_from=""
        rentalinstruction.checkout_until=""
        rentalinstruction.airport_instruction=""
        rentalinstruction.property_directions=""
        rentalinstruction.user_id=request.user.id
        rentalinstruction.rental_id=LastRow.id
        rentalinstruction.save()

        basicrates=BasicRates()
        basicrates.currency=""
        basicrates.basic_night=""
        basicrates.weekend_night=""
        basicrates.guest_number=""
        basicrates.minimum_stay=""
        basicrates.maximum_stay=""
        basicrates.user_id=request.user.id
        basicrates.rental_id=LastRow.id
        basicrates.save()

        rentalcleaning=RentalCleaning()
        rentalcleaning.cleaning_available=""
        rentalcleaning.cleaning_basis=""
        rentalcleaning.price=""
        rentalcleaning.user_id=request.user.id
        rentalcleaning.rental_id=LastRow.id
        rentalcleaning.save()

        rentaldeposit=RentalDeposit()
        rentaldeposit.security_deposit=""
        rentaldeposit.amount=""
        rentaldeposit.user_id=request.user.id
        rentaldeposit.rental_id=LastRow.id
        rentaldeposit.save()

        # path1 ="/rentals/overview/"
        # path2=str(LastInsertId)
        # path = path1+path2
        # messages.success(request, 'Row updated Successfully.')
        # return HttpResponseRedirect(path)

        return redirect("/super/rentals")


        
@login_required(login_url='/super/')  
def rental_ad(request):  
    amenities=Amenities.objects.all()
    activities=Activity.objects.all()
    policy=Policy.objects.all()

    context={
        'amenities':amenities,
        'activities':activities,
        'policy':policy
    }
    return render(request,"super/rentals/rental-ad.html",context) 

@login_required(login_url='/super/')  
def rental_add(request):  
    amenities=Amenities.objects.all()
    activities=Activity.objects.all()
    policy=Policy.objects.all()
    rentaltype=Rentaltype.objects.all()
    User = get_user_model().objects.all()

    context={
        'amenities':amenities,
        'activities':activities,
        'policy':policy,
        'users':User,
        'rentaltype':rentaltype
    }
    return render(request,"super/rentals/rental-add.html",context) 

@login_required(login_url='/super/')  
def rentals(request):
    rental= Rental.objects.all()
    return render(request,"super/rentals/rentals.html",{'rental':rental }) 


@login_required(login_url='/super/')  
def rental_edit(request, id):  
    rental = Rental.objects.get(id=id)
    amenities=Amenities.objects.all()
    activities=Activity.objects.all()
    policy=Policy.objects.all()
    rentaltype=Rentaltype.objects.all()

    context={
        'amenities':amenities,
        'activities':activities,
        'policy':policy,
        'rental':rental,
        'rentaltype':rentaltype
    }  
    return render(request,'super/rentals/rental-edit.html',context)  

@login_required(login_url='/super/')  
def rental_update(request, id): 
    if request.method == "POST": 
        rental= Rental.objects.get(id=id)
        rental.rental_name=request.POST.get('rental_name')
        if 'cover_image' in request.FILES:
           rental.cover_image = request.FILES['rental_logo']
        rental.rental_url=request.POST.get('rental_url')
        rental.rental_type_id=request.POST.get('rental_type')
        rental.amenities_id=request.POST.getlist('amenities[]')
        rental.activities_id=request.POST.getlist('activities[]')
        rental.policy_id=request.POST.getlist('policy[]')
        rental.rental_description=request.POST.get('rental_description')
       
        rental.save()
        return redirect("/super/rentals") 
   
    return render(request, 'super/rentals/rental-edit.html', {'rental': rental})  

@login_required(login_url='/super/')  
def rental_destroy(request, id):  
    rental= Rental.objects.get(id=id)  
    rental.delete()  
    return redirect("/super/rentals")  

def rental_basic(request,id):
    rental=Rental.objects.get(id=id)
    rentalbasic=RentalBasic.objects.get(rental_id=rental.id)
    rentaltype=Rentaltype.objects.all()
    context={
        'rentalbasic':rentalbasic,
        'rentaltype':rentaltype,
        'rental_id':id

    }
    return render(request,'super/rentals/rental-basic.html',context)

def rental_basic_update(request,id):
    if request.method == "POST": 
        rentalbasic=RentalBasic.objects.get(id=id)
        rentalbasic.rental_type=request.POST.get('rental_type')
        rentalbasic.rental_basis=request.POST.get('rental_basis')
        rentalbasic.floorspace=request.POST.get('floorspace')
        rentalbasic.floorspace_units=request.POST.get('floorspace_units')
        rentalbasic.grounds=request.POST.get('grounds')
        rentalbasic.grounds_units=request.POST.get('grounds_units')
        rentalbasic.floors_building=request.POST.get('floors_building')
        rentalbasic.entrance=request.POST.get('entrance')
        rentalbasic.rental_licence=request.POST.get('rental_licence')
        rentalbasic.save()   
    messages.success(request, 'Data Updated Successfully.')    
    return redirect(request.META.get('HTTP_REFERER'))    

@csrf_exempt
def sort(request):
    books = json.loads(request.POST.get('sort'))
    for b in books:
        book = get_object_or_404(RentalsGallery, pk=int(b['pk']))
        book.position = b['order']
        book.save()
    return JsonResponse(books)

def rentals_gallery(request, id):
    rental=Rental.objects.get(id=id)
    rentals_gallery=RentalsGallery.objects.filter(rental_id=rental.id).order_by('position')
    context={
    'rental':rental,
    'photos':rentals_gallery,
    'rental_id':id
    }
    #messages.success(request, ' Row Updated Successfully.')
    return render(request,'super/rentals/rental-photo.html',context)



def rentals_gallery_insert(request, id):  

    if request.method == "POST":

        rentals_gallery=RentalsGallery()

        rentals_gallery.image=request.FILES.get('image')

        rentals_gallery.user_id=request.user.id

        rentals_gallery.rental_id=id

        rentals_gallery.save()

        rental=rentals_gallery.save()

        data = {'is_valid': True, 'name': rental.image.name, 'url': rental.image.url}

        

    else:

        data = {'is_valid': False}
    messages.success(request, ' Row Updated Successfully.')
    return JsonResponse(data)

def gallery_destroy(request, id):  
    gallery = RentalsGallery.objects.get(id=id)  
    gallery.delete() 
    messages.success(request, ' Row deleted Successfully.')

    return redirect(request.META.get('HTTP_REFERER'))           

def rental_location(request,id):
    rental=Rental.objects.get(id=id)
    rentallocation=RentalLocation.objects.get(rental_id=rental.id)
    country=Country.objects.all()
    context={
        'rentallocation':rentallocation,
        'country':country,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-location.html',context)

def rental_location_update(request,id):
    if request.method == "POST": 
        rentallocation=RentalLocation.objects.get(id=id)
        rentallocation.country=request.POST.get("country")
        rentallocation.address=request.POST.get("address")
        rentallocation.apartment=request.POST.get("apartment")
        rentallocation.city=request.POST.get("city")
        rentallocation.state=request.POST.get("state")
        rentallocation.postal=request.POST.get("postal")
        rentallocation.save()
    messages.success(request, 'Data Updated Successfully.')    
    return redirect(request.META.get('HTTP_REFERER'))    

def rental_rooms(request,id):
    rental=Rental.objects.get(id=id)
    rooms=Room.objects.all()
    roomtype=Roomtype.objects.all()
    bed=Bed.objects.all()
    otherrooms=OtherRooms.objects.all()
    context={
        'rooms':rooms,
        'roomtype':roomtype,
        'bed':bed,
        'rental_id':id,
        'otherrooms':otherrooms,
        'rental':rental
    }
    return render(request,'super/rentals/rental-rooms.html',context)    

def rental_other_rooms_insert(request,id):
    rental=Rental.objects.get(id=id)
    
    if request.method == "POST": 
        rentalotherrooms=RentalOtherRooms()
        rentalotherrooms.other_rooms=request.POST.getlist('other_rooms[]') 
        rentalotherrooms.user_id=request.user.id
        rentalotherrooms.rental_id=id       
        rentalotherrooms.save()
    messages.success(request, 'Data Updated Successfully.') 
    return redirect(request.META.get('HTTP_REFERER'))   

def rental_amenities(request,id):
    rental=Rental.objects.get(id=id)
    rentalamenities=RentalAmenities.objects.get(rental_id=rental.id)
    amenities=Amenities.objects.all()
    amenitiestype=AmenitiesType.objects.all()
    
    
    context={
        'amenities':amenities,
        'amenitiestype':amenitiestype,
        'rentalamenities':rentalamenities,
        'rental_id':id,
        'amentitle':rentalamenities.amenities

    }
  
   
    
    return render(request,'super/rentals/rental-amenities.html',context) 



def rental_amenities_update(request,id):
    if request.method == "POST": 
        rentalamenities=RentalAmenities.objects.get(id=id)
        rentalamenities.amenities=request.POST.getlist('amenities[]') 
        rentalamenities.save()
    messages.success(request, 'Data Updated Successfully.') 
    return redirect(request.META.get('HTTP_REFERER'))    


def rental_basic_rates(request,id):
    rental=Rental.objects.get(id=id)
    basicrates=BasicRates.objects.get(rental_id=rental.id)
    currency=Currency.objects.all()
    context={
        'basicrates':basicrates,
        'currency':currency,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-basic-rates.html',context)

def rental_basic_rates_update(request,id):  
    if request.method == "POST": 
        basicrates=BasicRates.objects.get(id=id)
        basicrates.currency=request.POST.get('currency')
        basicrates.basic_night=request.POST.get('basic_night')
        basicrates.weekend_night=request.POST.get('weekend_night')
        basicrates.guest_number=request.POST.get('guest_number')
        basicrates.minimum_stay=request.POST.get('minimum_stay')
        basicrates.maximum_stay=request.POST.get('maximum_stay')
        basicrates.checkin_days=request.POST.getlist('checkin_days[]')
        basicrates.checkout_days=request.POST.getlist('checkout_days[]')
        next = request.POST.get('next', '/')
        basicrates.save()
    #return HttpResponseRedirect(next)    
    # return redirect('/rentals/seasonal-rates')  
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))    


def rental_seasonal_rates(request,id):
    rental=Rental.objects.get(id=id)
    seasonalrates=SeasonalRates.objects.filter(rental_id=rental.id)
    context={        
        'rental_id':id,
        'seasonalrates':seasonalrates,
        'rental':rental
    }
    # seasonalrates=SeasonalRates.objects.get(rental_id=rental.id)
    return render(request,'super/rentals/rental-seasonal-rates.html',context)

def rental_seasonal_rates_insert(request,id):
    rental=Rental.objects.get(id=id)
    if request.method == "POST":
        seasonalrates=SeasonalRates()
        seasonalrates.season_name=request.POST.get('season_name')
        seasonalrates.start_date=request.POST.get('start_date')
        seasonalrates.end_date=request.POST.get('end_date')
        seasonalrates.basic_night=request.POST.get('basic_night')
        seasonalrates.weekend_night=request.POST.get('weekend_night')
        seasonalrates.minimum_stay=request.POST.get('minimum_stay')
        seasonalrates.maximum_stay=request.POST.get('maximum_stay')
        seasonalrates.checkin_days=request.POST.getlist('checkin_days[]')
        seasonalrates.checkout_days=request.POST.getlist('checkout_days[]')
        seasonalrates.user_id=request.user.id
        seasonalrates.rental_id=id
        seasonalrates.save()
        messages.success(request, 'Data Added Successfully.')
        return redirect(request.META.get('HTTP_REFERER'))
    #return render(request,'users/rentals/rental-seasonal-rates.html',{'rental':rental})        


def rental_seasonal_rates_edit(request,id):
    rental=Rental.objects.get(id=id)
    seasonalrates=SeasonalRates.objects.get(rental_id=rental.id)
    return render(request,'super/rentals/rental-seasonal-rates.html',{'seasonalrates':seasonalrates})


def rental_seasonal_rates_update(request,id):  
    if request.method == "POST": 
        seasonalrates=SeasonalRates.objects.get(id=id)
        seasonalrates.season_name=request.POST.get('season_name')
        seasonalrates.start_date=request.POST.get('start_date')
        seasonalrates.end_date=request.POST.get('end_date')
        seasonalrates.basic_night=request.POST.get('basic_night')
        seasonalrates.weekend_night=request.POST.get('weekend_night')
        seasonalrates.minimum_stay=request.POST.get('minimum_stay')
        seasonalrates.maximum_stay=request.POST.get('maximum_stay')
        seasonalrates.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))    

def rental_seasonal_destroy(request, id):  
    rentalSeasonal = SeasonalRates.objects.get(id=id)  
    rentalSeasonal.delete()
    messages.success(request, 'Row deleted Successfully.')  
    return redirect(request.META.get('HTTP_REFERER'))

def rental_discount(request,id):
    rental=Rental.objects.get(id=id)
    longstaydiscount=LongStayDiscount.objects.get(rental_id=rental.id)
    earlybirddiscount=EarlyBirdDiscount.objects.get(rental_id=rental.id)
    context={
        'longstaydiscount':longstaydiscount,
        'earlybirddiscount':earlybirddiscount,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-discount.html',context)

def long_stay_discount_update(request,id):
    if request.method == "POST": 
        longstaydiscount=LongStayDiscount.objects.get(id=id)
        longstaydiscount.seven_nights=request.POST.get('seven_nights')
        longstaydiscount.fourteen_nights=request.POST.get('fourteen_nights') 
        longstaydiscount.twenty_one_nights=request.POST.get('twenty_one_nights') 
        longstaydiscount.twenty_eight_nights=request.POST.get('twenty_eight_nights') 
        longstaydiscount.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))  

def early_bird_discount_update(request,id):
    if request.method == "POST": 
        earlybirddiscount=EarlyBirdDiscount.objects.get(id=id)
        earlybirddiscount.booking_less=request.POST.get('booking_less')
        earlybirddiscount.booking_less_discount=request.POST.get('booking_less_discount') 
        earlybirddiscount.booking_more=request.POST.get('booking_more') 
        earlybirddiscount.booking_more_discount=request.POST.get('booking_more_discount') 
        earlybirddiscount.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))      




def rental_additional_info(request,id):
    rental=Rental.objects.get(id=id)
    rentalcleaning=RentalCleaning.objects.get(rental_id=rental.id)
    rentaldeposit=RentalDeposit.objects.get(rental_id=rental.id)
    rentaltax=RentalTax.objects.filter(rental_id=rental.id)
    extraservices=ExtraServices.objects.filter(rental_id=rental.id)
    customservices=CustomServices.objects.filter(rental_id=rental.id)
    
    context={
        'rentalcleaning':rentalcleaning,
        'rentaldeposit':rentaldeposit,
        'rental':rental,
        'rental_id':id,
        'rentaltax':rentaltax,
        'extraservices':extraservices,
        'customservices':customservices
    }
    return render(request,'super/rentals/rental-additional-info.html',context)

def rental_cleaning_update(request,id):
    if request.method == "POST": 
        rentalcleaning=RentalCleaning.objects.get(id=id)
        rentalcleaning.cleaning_available=request.POST.get('cleaning_available')
        rentalcleaning.cleaning_basis=request.POST.get('cleaning_basis') 
        rentalcleaning.price=request.POST.get('price') 
        rentalcleaning.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))   

def rental_deposit_update(request,id):
    if request.method == "POST": 
        rentaldeposit=RentalDeposit.objects.get(id=id)
        rentaldeposit.security_deposit=request.POST.get('security_deposit')
        rentaldeposit.amount=request.POST.get('amount') 
        rentaldeposit.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))   

def rental_tax_insert(request,id):
    rental=Rental.objects.get(id=id)
    if request.method == "POST": 
        rentaltax=RentalTax()
        rentaltax.tax_type=request.POST.get('tax_type')
        rentaltax.fee_basis=request.POST.get('fee_basis') 
        rentaltax.percentage=request.POST.get('percentage')
        rentaltax.amountin=request.POST.get('amountin')
        rentaltax.user_id=request.user.id
        rentaltax.rental_id=id
        rentaltax.save()
        messages.success(request, 'Data Updated Successfully.')
        return redirect(request.META.get('HTTP_REFERER'))  
    #return render(request,'/users/rentals/rental-additional-info.html',{'rental':rental}) 

def rental_tax_update(request,id):
    rentaltax=RentalTax.objects.get(id=id)
    if request.method == "POST": 
        rentaltax.tax_type=request.POST.get('tax_type')
        rentaltax.fee_basis=request.POST.get('fee_basis') 
        rentaltax.percentage=request.POST.get('percentage')
        rentaltax.amountin=request.POST.get('amountin')
        rentaltax.user_id=request.user.id
        rentaltax.rental_id=id
        rentaltax.save()
        messages.success(request, 'Data Updated Successfully.')
        return redirect(request.META.get('HTTP_REFERER'))


def rental_tax_destroy(request, id):  
    rentaltax = RentalTax.objects.get(id=id)  
    rentaltax.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect(request.META.get('HTTP_REFERER'))

def rental_extra_services_insert(request,id):
    rental=Rental.objects.get(id=id)
    if request.method == "POST": 
        extraservices=ExtraServices()
        extraservices.service_name=request.POST.get('service_name')
        extraservices.service_provided=request.POST.get('service_provided') 
        extraservices.fee_basis=request.POST.get('fee_basis')
        extraservices.service_price=request.POST.get('service_price')
        extraservices.earliest_guest_order=request.POST.get('earliest_guest_order')
        extraservices.service_provided=request.POST.get('service_provided') 
        extraservices.latest_guest_order=request.POST.get('latest_guest_order')
        extraservices.guest_cancel_order=request.POST.get('guest_cancel_order')
        extraservices.extra_message=request.POST.get('extra_message')
        extraservices.user_id=request.user.id
        extraservices.rental_id=id
        extraservices.save()
        messages.success(request, 'Data Updated Successfully.')
        return redirect(request.META.get('HTTP_REFERER'))  
    #return render(request,'/users/rentals/rental-additional-info.html',{'rental':rental})    

def rental_custom_services_insert(request,id):
    rental=Rental.objects.get(id=id)
    if request.method == "POST": 
        customservices=CustomServices()
        customservices.custom_service_name=request.POST.get('custom_service_name')
        customservices.custom_service_provided=request.POST.get('custom_service_provided') 
        customservices.custom_fee_basis=request.POST.get('custom_fee_basis')
        customservices.custom_service_price=request.POST.get('custom_service_price')
        customservices.custom_earliest_guest_order=request.POST.get('custom_earliest_guest_order')
        customservices.custom_service_provided=request.POST.get('custom_service_provided') 
        customservices.custom_latest_guest_order=request.POST.get('custom_latest_guest_order')
        customservices.custom_guest_cancel_order=request.POST.get('custom_guest_cancel_order')
        customservices.custom_extra_message=request.POST.get('custom_extra_message')
        customservices.user_id=request.user.id
        customservices.rental_id=id
        customservices.save()
        messages.success(request, 'Data Updated Successfully.')
        return redirect(request.META.get('HTTP_REFERER'))  
    #return render(request,'/users/rentals/rental-additional-info.html',{'rental':rental})         



def rental_house_rules(request,id):
    rental=Rental.objects.get(id=id)
    houserules=HouseRules.objects.get(rental_id=rental.id)
    context={
        'houserules':houserules,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-house-rules.html',context) 

def rental_house_rules_update(request,id):
    if request.method == "POST": 
        houserules=HouseRules.objects.get(id=id)
        houserules.for_kid=request.POST.get('for_kid')
        houserules.wheelchair_access=request.POST.get('wheelchair_access')
        houserules.parties_allowed=request.POST.get('parties_allowed')
        houserules.smoking_allowed=request.POST.get('smoking_allowed')
        houserules.pets=request.POST.get('pets')
        houserules.house_rules=request.POST.get('house_rules')
        houserules.save()
        messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))         

def rental_policy(request,id):
    rental=Rental.objects.get(id=id)
    rentalpolicy=RentalPolicy.objects.get(rental_id=rental.id)
    context={
        'rentalpolicy':rentalpolicy,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-policy.html',context) 

def rental_policy_update(request,id):
    if request.method == "POST": 
        rentalpolicy=RentalPolicy.objects.get(id=id)
        rentalpolicy.name=request.POST.get('name')
        rentalpolicy.description=request.POST.get('description')
        rentalpolicy.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))     



def rental_instruction(request,id):
    rental=Rental.objects.get(id=id)
    rentalinstruction=RentalInstruction.objects.get(rental_id=rental.id)
    country=Country.objects.all()
    context={
        'rentalinstruction':rentalinstruction,
        'country':country,
        'rental_id':id
    }
    return render(request,'super/rentals/rental-instructions.html',context)                           

def rental_instruction_update(request,id):
    if request.method == "POST": 
        rentalinstruction=RentalInstruction.objects.get(id=id)
        rentalinstruction.checkin_instruction=request.POST.get('checkin_instruction')
        rentalinstruction.checkout_instruction=request.POST.get('checkout_instruction')
        rentalinstruction.checkin_contact=request.POST.get('checkin_contact')
        rentalinstruction.key_collection=request.POST.get('key_collection')
        rentalinstruction.telephone_country=request.POST.get('telephone_country')
        rentalinstruction.telephone_number=request.POST.get('telephone_number')
        rentalinstruction.instructions=request.POST.get('instructions')
        rentalinstruction.attach_instruction=request.FILES.get('attach_instruction')
        rentalinstruction.checkin_from=request.POST.get('checkin_from')
        rentalinstruction.checkout_until=request.POST.get('checkout_until')
        rentalinstruction.airport_instruction=request.POST.get('airport_instruction')
        rentalinstruction.property_directions=request.POST.get('property_directions')
        rentalinstruction.save()
    messages.success(request, 'Data Updated Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))  

def rental_select_channels(request,id):
    channels=Channel.objects.all()
    context={
        'channels':channels,
        'rental_id':id
    }
    return render (request,'super/rentals/rental-channels.html',context)    
        
# Rental Code end  


# Invoice code start

class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'super/invoice/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))
        try:

            update_status_for_invoices = int(request.POST['status'])
        except KeyError:
            update_status_for_invoices = "Guest"

        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('/super/invoice/')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    # heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = InvoiceItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = InvoiceItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.data["customer"],
                    customer_email=form.data["customer_email"],
                    billing_address= form.data["billing_address"],
                   
                    message=form.data["message"],
                    )
            # invoice.save()
            
        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                if service and description and quantity and rate:
                    amount = float(rate)*float(quantity)
                    total += amount
                    InvoiceItem(customer=invoice,
                            service=service,
                            description=description,
                            quantity=quantity,
                            rate=rate,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/super/invoice')
    context = {
        "title" : "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'super/invoice/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    invoiceitem = invoice.invoiceitem_set.all()

    context = {
        "company": {
            "name": "Apex Websoft",
            "address" :"Noida Up india",
            "phone": "7303699947",
            "email": "amanrajput110298@gmail.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_email": invoice.customer_email,
       
        "billing_address": invoice.billing_address,
        "message": invoice.message,
        "invoiceitem": invoiceitem,

    }
    return render(request, 'super/invoice/pdf_template.html', context)

def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    # pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response


def change_status(request):
    return redirect('super:invoice:invoice-list')

def view_404(request,  *args, **kwargs):

    return redirect('super:invoice:invoice-list')  

@login_required(login_url='/super/')  
def company_insert(request):  
    if request.method == "POST":
        companyprofile=CompanyProfile()
        companyprofile.company_name=request.POST.get('company_name') 
        companyprofile.company_logo=request.FILES.get('company_logo') 
        companyprofile.company_email=request.POST.get('company_email') 
        companyprofile.company_tel=request.POST.get('company_tel') 
        companyprofile.company_address=request.POST.get('company_address') 
        companyprofile.user_id=request.POST.get('user_id') 
        companyprofile.save()

        return redirect('/super/company')

@login_required(login_url='/super/')  
def company_add(request): 
    User = get_user_model().objects.all() 
    return render(request,'super/invoice/company-add.html',{'users':User})  

@login_required(login_url='/super/')      
def company(request):  
    companies = CompanyProfile.objects.all()  
    return render(request,"super/invoice/company.html",{'companies':companies})  

@login_required(login_url='/super/')  
def company_edit(request, id):  
    company= CompanyProfile.objects.get(id=id)  
    return render(request,'super/invoice/company-edit.html', {'company':company})  

@login_required(login_url='/super/')  
def company_update(request, id):  
    company= CompanyProfile.objects.get(id=id)
    if request.method == "POST":
        companyprofile=CompanyProfile()
        companyprofile.company_name=request.POST.get('company_name') 
        companyprofile.company_logo=request.FILES.get('company_logo') 
        companyprofile.company_email=request.POST.get('company_email') 
        companyprofile.company_tel=request.POST.get('company_tel') 
        companyprofile.company_address=request.POST.get('company_address') 
        companyprofile.save()

        return redirect('/super/company')
  
   
     
    return render(request, 'super/invoice/company-edit.html', {'company': company})  

@login_required(login_url='/super/')  
def company_destroy(request, id):  
    company = CompanyProfile.objects.get(id=id)  
    company.delete()  
    return redirect("/super/company")                      


# def rentals_gallery_insert(request,id):
#     if request.method == "POST":
#         if request.is_ajax():
#             rental=Rental()
#             rentals_gallery=RentalsGallery()
#             rentals_gallery.image=request.FILES.getlist('image')
#             image_list=[]
#             for image in image:
#                 image_list.append(RentalsGallery(image=image))
#             if  image_list : 
#                 RentalsGallery.objects.bulk_create(image_list)
#             rentals_gallery.user_id=request.user.id
#             rentals_gallery.rental=Rental.objects.get(id=id)
#             rentals_gallery.save()
#             messages.success(request, ' Row added Successfully.')
#             return redirect(request.META.get('HTTP_REFERER'))
#     return render(request,'super/rentals/rentals-gallery.html',{'rental':rental})   

# @ensure_csrf_cookie
# def rentals_gallery_insert(request):
#     if request.method == "GET":
#         return render(request, 'super/rentals/rentals-gallery.html', )
#     if request.method == 'POST':
#         image = request.FILES.getlist('files[]', None)
#         print(image)
#         for f in image:
#             handle_uploaded_file(f)
#         return JsonResponse({'msg':'<span style="color: green;">File successfully uploaded</span>'})
#     else:
#         return render(request, 'super/rentals/rentals-gallery.html', )

# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# def rentals_gallery(request,id):
    
#     rental=Rental.objects.get(id=id)
#     rentals_gallery=RentalsGallery.objects.filter(rental_id=rental.id)
    

#     context={
        
#         'rental':rental,
#         'rentals_gallery':rentals_gallery
#     }
#     return render(request,'super/rentals/rentals-gallery.html',context)    

# def rentals_gallery_add(request):
#     return render(request,'super/rentals/rentals-gallery-add.html')
  

# Rental-Gallery Code end

# Attributes code start

@login_required(login_url='/super/')
def attributes_insert(request):  
    if request.method == "POST":
        attributes=Attributes()
        attributes.name=request.POST.get('name')  
        attributes.status=request.POST.get('status')
        attributes.user_id= request.POST.get('user_id')
        attributes.save()
        messages.success(request, ' Row added Successfully.')

    return redirect('/super/attributes')   

@login_required(login_url='/super/')
def attributes_add(request):
    User = get_user_model().objects.all()
    return render (request,"super/attributes/attributes-add.html",{'users':User})     
       
@login_required(login_url='/super/') 
def attributes(request):
    attributes = Attributes.objects.all()  
    return render(request,"super/attributes/attributes.html",{'attributes':attributes})  

@login_required(login_url='/super/')
def attributes_edit(request, id):  
    attributes = Attributes.objects.get(id=id)  
    return render(request,'super/attributes/attributes-edit.html', {'attributes':attributes})  

@login_required(login_url='/super/')
def attributes_update(request, id):  
    attributes = Attributes.objects.get(id=id) 
    if request.method == "POST":
        attributes.name=request.POST.get('name')  
        attributes.status=request.POST.get('status')
        attributes.save()
        messages.success(request, ' Row updated Successfully.')

    return redirect('/super/attributes')  
   

@login_required(login_url='/super/')
def attributes_destroy(request, id):  
    attributes = Attributes.objects.get(id=id)  
    attributes.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/attributes")

# Attributes code end      

def calendar(request):
    rental=Rental.objects.filter(user_id=request.user.id)    
    return render(request,'super/calendar/calendar.html',{'rental':rental})


def reports(request):
    if request.method=="POST":
        fromdate = request.POST.get('from_date')
        todate = request.POST.get('to_date')
        user_id=request.POST.get('user_id')
        search=Bookings.objects.raw('select id,booking_type,first_name,last_name,created_at from bookings where created_at between"'+fromdate+'" and " '+todate+'" ')
        usersearch=Bookings.objects.filter(user_id=user_id).values()
        context={
            'data':search,    
            'data':usersearch,
            
        }
        return render(request,'super/reports/reports.html',context)
    else:
        bookings = Bookings.objects.all()
        User = get_user_model().objects.all() 
        context={
            'data':bookings,
            'users':User
        }
        return render(request,'super/reports/reports.html',context)

# Category code start 

@login_required(login_url='/super/')
def category_insert(request):
    if request.method == "POST": 
        category=Category()
        category.title=request.POST.get('title')
        category.icon=request.FILES.get('icon')
        category.status=request.POST.get('status')
        category.save()
        messages.success(request, ' Row added Successfully.')
    return redirect ("/super/partners-category")

@login_required(login_url='/super/')     
def category_add(request):
    return render(request,"super/partner/category-add.html")  

@login_required(login_url='/super/')
def category(request):  
    category = Category.objects.all()  
    return render(request,"super/partner/category.html",{'category':category})  

@login_required(login_url='/super/')
def category_edit(request, id):  
    category= Category.objects.get(id=id)  
    return render(request,'super/partner/category-edit.html', {'category':category})  

@login_required(login_url='/super/')
def category_update(request, id):  
    category= Category.objects.get(id=id)  
    if request.method == "POST": 
        category.title=request.POST.get('title')
        if 'icon' in request.FILES:
           category.icon = request.FILES['icon']
        category.status=request.POST.get('status')
        category.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect ("/super/partners-category")
   
    return render(request, 'super/partner/category-edit.html')  

@login_required(login_url='/super/')
def category_destroy(request, id):  
    category = Category.objects.get(id=id)  
    category.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/partner-category") 

# Category Code End    

# Partner code start 

@login_required(login_url='/super/')
def partner_insert(request):
    if request.method == "POST": 
        partner=Partner()
        partner.title=request.POST.get('title')
        partner.url=request.POST.get('url')
        partner.subtitle=request.POST.get('subtitle')
        partner.description=request.POST.get('description')
        partner.shortdescription=request.POST.get('shortdescription')
        partner.category_id=request.POST.get('category')
        partner.image=request.FILES.get('image')
        partner.status=request.POST.get('status')
        partner.save()
        messages.success(request, ' Row added Successfully.')
    return redirect ("/super/partner")

@login_required(login_url='/super/')     
def partner_add(request):
    category=Category.objects.all()
    return render(request,"super/partner/partner-add.html",{'category':category})  

@login_required(login_url='/super/')
def partner(request):  
    partner = Partner.objects.all()  
    return render(request,"super/partner/partner.html",{'partner':partner})  

@login_required(login_url='/super/')
def partner_edit(request, id):  
    partner= Partner.objects.get(id=id)
    category=Category.objects.all() 
    context={
        'partner':partner,
        'category':category

    } 
    return render(request,'super/partner/partner-edit.html', context)  

@login_required(login_url='/super/')
def partner_update(request, id):    
    if request.method == "POST": 
        partner= Partner.objects.get(id=id)
        partner.title=request.POST.get('title')
        partner.url=request.POST.get('url')
        partner.subtitle=request.POST.get('subtitle')
        partner.description=request.POST.get('description')
        partner.shortdescription=request.POST.get('shortdescription')
        partner.category_id=request.POST.get('category')
        if 'image' in request.FILES:
           partner.image = request.FILES['image']
        partner.status=request.POST.get('status')
        partner.save()
        messages.success(request, ' Row updated Successfully.')
        return redirect ("/super/partner")
   
    return render(request, 'super/partner/partner-edit.html')  

@login_required(login_url='/super/')
def partner_destroy(request, id):  
    partner = Partner.objects.get(id=id)  
    partner.delete()
    messages.success(request, ' Row deleted Successfully.')  
    return redirect("/super/partner") 

# Partner Code End  

# Subscription Code start

def subscription_insert(request):
    if request.method == "POST":
        sub=Subscription()
        sub.title=request.POST.get('title')  
        sub.subtitle=request.POST.get('subtitle')
        sub.price=request.POST.get('price')
        sub.description=request.POST.get('description')
        sub.tenure=request.POST.get('tenure')
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/subscription')

def subscription_add(request):
    return render(request,"super/subscription/subscription-add.html")


def subscription(request):
    subscription=Subscription.objects.all()
    return render(request,"super/subscription/subscription.html",{'subscription':subscription})

def subscription_edit(request,id):
    subscription=Subscription.objects.get(id=id)
    return render(request,"super/subscription/subscription-edit.html",{'subscription':subscription})

def subscription_update(request,id):
    if request.method == "POST":
        sub=Subscription.objects.get(id=id)
        sub.title=request.POST.get('title')  
        sub.subtitle=request.POST.get('subtitle')
        sub.price=request.POST.get('price')
        sub.description=request.POST.get('description')
        sub.tenure=request.POST.get('tenure')
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/subscription')

def subscription_destroy(request,id):
    sub=Subscription.objects.get(id=id)
    sub.delete()
    return redirect('/super/subscription')

# Country Code end
def country_insert(request):
    if request.method == "POST":
        sub=Country()
        sub.name=request.POST.get('name')  
        sub.code=request.POST.get('code')
        sub.country_code=request.POST.get('country_code')
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/country')

def country_add(request):
    return render(request,"super/systems/country-add.html")

def country(request):
    countries=Country.objects.all()
    return render(request,"super/systems/country.html",{'countries':countries})

def country_edit(request,id):
    country=Country.objects.get(id=id)
    return render(request,"super/systems/country-edit.html",{'country':country})

def country_update(request,id):
    if request.method == "POST":
        sub=Country.objects.get(id=id)
        sub.name=request.POST.get('name')  
        sub.code=request.POST.get('code')
        sub.country_code=request.POST.get('country_code')
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/country')

def country_destroy(request,id):
    sub=Country.objects.get(id=id)
    sub.delete()
    return redirect('/super/country')

# Country Code end

# Property Role Code end
def property_role_insert(request):
    if request.method == "POST":
        sub=PropertyRole()
        sub.title=request.POST.get('title')  
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/property-role')

def property_role_add(request):
    return render(request,"super/systems/property-role-add.html")

def property_role(request):
    propertyrole=PropertyRole.objects.all()
    return render(request,"super/systems/property-role.html",{'propertyrole':propertyrole})

def property_role_edit(request,id):
    propertyrole=PropertyRole.objects.get(id=id)
    return render(request,"super/systems/property-role-edit.html",{'propertyrole':propertyrole})

def property_role_update(request,id):
    if request.method == "POST":
        sub=PropertyRole.objects.get(id=id)
        sub.title=request.POST.get('title')  
        sub.status=request.POST.get('status')
        sub.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/property-role')

def property_role_destroy(request,id):
    sub=PropertyRole.objects.get(id=id)
    sub.delete()
    return redirect('/super/property-role')

# Property Role Code end

# Room Type Code start
def room_type_insert(request):
    if request.method == "POST":
        rt=Roomtype()
        rt.title=request.POST.get('title') 
        rt.icon=request.FILES.get('icon')   
        rt.status=request.POST.get('status')
        rt.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/room-type')

def room_type_add(request):
    return render(request,"super/rooms/room-type-add.html")

def room_type(request):
    rt=Roomtype.objects.all()
    return render(request,"super/rooms/room-type.html",{'rt':rt})

def room_type_edit(request,id):
    rt=Roomtype.objects.get(id=id)
    return render(request,"super/ROOMS/room-type-edit.html",{'rt':rt})

def room_type_update(request,id):
    if request.method == "POST":
        rt=Roomtype.objects.get(id=id)
        rt.title=request.POST.get('title') 
        rt.icon=request.FILES.get('icon')   
        rt.status=request.POST.get('status')
        rt.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/room-type')

def room_type_destroy(request,id):
    rt=Roomtype.objects.get(id=id)
    rt.delete()
    return redirect('/super/room-type')

# Room Type Code end

# Room  Code start
def room_insert(request):
    if request.method == "POST":
        room=Room()
        room.room_type_id=request.POST.get('room_type')
        room.title=request.POST.get('title') 
        room.icon=request.FILES.get('icon')   
        room.status=request.POST.get('status')
        room.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/rooms')

def room_add(request):
    rt=Roomtype.objects.all()
    return render(request,"super/rooms/room-add.html",{'rt':rt})

def rooms(request):
    room=Room.objects.all()
    return render(request,"super/rooms/room.html",{'room':room})

def room_edit(request,id):
    room=Room.objects.get(id=id)
    rt=Roomtype.objects.all()
    context={
        'room':room,
        'rt':rt
    }
    return render(request,"super/rooms/room-edit.html",context)

def room_update(request,id):
    if request.method == "POST":
        room=Room.objects.get(id=id)
        room.room_type_id=request.POST.get('room_type')
        room.title=request.POST.get('title') 
        room.icon=request.FILES.get('icon')   
        room.status=request.POST.get('status')
        room.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/rooms')

def room_destroy(request,id):
    room=Room.objects.get(id=id)
    room.delete()
    return redirect('/super/rooms')

# Room  Code end

# Room  Code start
def bed_insert(request):
    if request.method == "POST":
        bed=Bed()
        bed.title=request.POST.get('title') 
        bed.icon=request.FILES.get('icon')   
        bed.status=request.POST.get('status')
        bed.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/beds')

def bed_add(request):
    return render(request,"super/rooms/bed-add.html")

def beds(request):
    bed=Bed.objects.all()
    return render(request,"super/rooms/beds.html",{'bed':bed})

def bed_edit(request,id):
    bed=Bed.objects.get(id=id)
    context={
        'bed':bed
        
    }
    return render(request,"super/rooms/bed-edit.html",context)

def bed_update(request,id):
    if request.method == "POST":
        bed=Bed.objects.get(id=id)
        bed.title=request.POST.get('title') 
        bed.icon=request.FILES.get('icon')   
        bed.status=request.POST.get('status')
        bed.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/beds')

def bed_destroy(request,id):
    bed=Bed.objects.get(id=id)
    bed.delete()
    return redirect('/super/beds')

# Bed  Code end

# Other-Rooms  Code start
def other_room_insert(request):
    if request.method == "POST":
        otherrooms=OtherRooms()
        otherrooms.title=request.POST.get('title')    
        otherrooms.status=request.POST.get('status')
        otherrooms.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/other-rooms')

def other_room_add(request):
    return render(request,"super/rooms/other-room-add.html")

def other_rooms(request):
    otherrooms=OtherRooms.objects.all()
    return render(request,"super/rooms/other-rooms.html",{'otherrooms':otherrooms})

def other_rooms_edit(request,id):
    otherrooms=OtherRooms.objects.get(id=id)
    context={
        'otherrooms':otherrooms
        
    }
    return render(request,"super/rooms/other-room-edit.html",context)

def other_room_update(request,id):
    if request.method == "POST":
        otherrooms=OtherRooms.objects.get(id=id)
        otherrooms.title=request.POST.get('title')    
        otherrooms.status=request.POST.get('status')
        otherrooms.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/other-rooms')

def other_room_destroy(request,id):
    otherrooms=OtherRooms.objects.get(id=id)
    otherrooms.delete()
    return redirect('/super/other-rooms')

# Other-Rooms  Code end

# Services  Code start

def services(request):
    services=Services.objects.all()
    return render(request,"super/services/services.html",{'services':services})

def services_insert(request):
    if request.method == "POST":
        services=Services()
        services.title=request.POST.get('title')
        services.status=request.POST.get('status')
        services.save()
        messages.success(request, ' Row added Successfully.')
    return redirect('/super/services')

def services_add(request):
    return render(request,"super/services/services-add.html")

def services_edit(request,id):
    services=Services.objects.get(id=id)
    context={
        'services':services
        
    }
    return render(request,"super/services/services-edit.html",context)

def services_update(request,id):
    if request.method == "POST":
        services=Services.objects.get(id=id)
        services.title=request.POST.get('title') 
        services.status=request.POST.get('status')
        services.save()
        messages.success(request, ' Row updated Successfully.')
    return redirect('/super/services')

def services_destroy(request,id):
    services=Services.objects.get(id=id)
    services.delete()
    return redirect('/super/services')

# Services Code end

def change_user_password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return redirect('/super/user-profile')

    context = {'user': user}
    return render(request, "super/users/user-indivisual-profile.html", context)