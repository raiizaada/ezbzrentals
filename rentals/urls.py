from django.urls import path
from . import views
from django.urls import path  
from django.conf import settings  
from django.conf.urls.static import static 

app_name = 'rentals'  
urlpatterns = [

# index
    path('super/dashboard',views.index,name='index'),

# authentication
    #path('super/register', views.registerPage, name="register"),
	path('super/', views.auth_view, name="login"),   
	path('super/logout', views.logoutUser, name="logout"),  

#user management       
    path('super/users',views.users),
    path('super/user-insert',views.user_insert),
    path('super/user-add',views.user_add),
    path('super/user-edit/<int:id>',views.user_edit),
    path('super/user-update/<int:id>',views.user_update),
    path('super/user-delete/<int:id>',views.user_delete),
    path('super/user-profile',views.user_profile),
    path('super/user-profile-edit/<int:id>',views.user_profile_edit),
    path('super/user-profile-update/<int:id>',views.user_profile_update),
    path('super/user-profile-delete/<int:id>',views.user_profile_delete),
    path('super/user-indivisual-profile/<int:id>',views.user_indivisual_profile),
    path('super/user-indivisual-profile-update/<int:id>',views.user_indivisual_profile_update),
# channels  
    path('super/channel-add',views.channel_add),  
    path('super/channel-insert',views.channel_insert), 
    path('super/channels',views.channels),  
    path('super/channel-edit/<int:id>', views.channel_edit),  
    path('super/channel-update/<int:id>', views.channel_update),  
    path('super/channel-delete/<int:id>', views.channel_destroy), 

# amenities
    path('super/amenities-insert',views.amenities_insert),  
    path('super/amenities-add',views.amenities_add), 
    path('super/amenities',views.amenities),  
    path('super/amenities-edit/<int:id>', views.amenities_edit),  
    path('super/amenities-update/<int:id>', views.amenities_update),  
    path('super/amenities-delete/<int:id>', views.amenities_destroy),
    path('super/amenities-type',views.amenities_type), 
    path('super/amenities-type-insert',views.amenities_type_insert),  
    path('super/amenities-type-add',views.amenities_type_add),  
    path('super/amenities-type-edit/<int:id>', views.amenities_type_edit),  
    path('super/amenities-type-update/<int:id>', views.amenities_type_update),  
    path('super/amenities-type-delete/<int:id>', views.amenities_type_destroy),
    
# activity
    path('super/activity',views.activity),  
    path('super/activity-add',views.activity_add),
    path('super/activity-insert',views.activity_insert),  
    path('super/activity-edit/<int:id>', views.activity_edit),  
    path('super/activity-update/<int:id>', views.activity_update),  
    path('super/activity-delete/<int:id>', views.activity_destroy),

# rentals
    path('super/rental-add',views.rental_add),
    path('super/rental-insert',views.rental_insert),
    path('super/rentals',views.rentals),  
    path('super/rental-edit/<int:id>', views.rental_edit),  
    path('super/rental-update/<int:id>', views.rental_update),  
    path('super/rental-delete/<int:id>', views.rental_destroy),

# rental-type  
    path('super/rental-type-add',views.rental_type_add),  
    path('super/rental-type-insert',views.rental_type_insert), 
    path('super/rental-type',views.rental_type),  
    path('super/rental-type-edit/<int:id>', views.rental_type_edit),  
    path('super/rental-type-update/<int:id>', views.rental_type_update),  
    path('super/rental-type-delete/<int:id>', views.rental_type_destroy), 
    
# tax
    path('super/tax-add',views.tax_add), 
    path('super/tax-insert',views.tax_insert), 
    path('super/tax',views.tax),  
    path('super/tax-edit/<int:id>', views.tax_edit),  
    path('super/tax-update/<int:id>', views.tax_update),  
    path('super/tax-delete/<int:id>', views.tax_destroy), 
    
# Tax Type
    path('super/tax-type', views.tax_type),
    path('super/tax-type-add', views.tax_type_add),
    path('super/tax-type-insert', views.tax_type_insert),
    path('super/tax-type-edit/<int:id>', views.tax_type_edit), 
    path('super/tax-type-update/<int:id>', views.tax_type_update),  
    path('super/tax-type-delete/<int:id>', views.tax_type_destroy), 
    
# Policy
    path('super/policy', views.policy),
    path('super/policy-add', views.policy_add),
    path('super/policy-insert', views.policy_insert),
    path('super/policy-edit/<int:id>', views.policy_edit), 
    path('super/policy-update/<int:id>', views.policy_update),
    path('super/policy-delete/<int:id>', views.policy_destroy), 
    
# Rate Type 
    path('super/rate-type', views.rate_type),
    path('super/rate-type-add', views.rate_type_add),
    path('super/rate-type-insert', views.rate_type_insert),
    path('super/rate-type-edit/<int:id>', views.rate_type_edit), 
    path('super/rate-type-update/<int:id>', views.rate_type_update),  
    path('super/rate-type-delete/<int:id>', views.rate_type_destroy), 

# Rate 
    path('super/rate', views.rate),
    path('super/rate-add', views.rate_add),
    path('super/rate-insert', views.rate_insert),
    path('super/rate-edit/<int:id>', views.rate_edit), 
    path('super/rate-update/<int:id>', views.rate_update),  
    path('super/rate-delete/<int:id>', views.rate_destroy), 

# Booking
    path('super/bookings',views.booking),
    path('super/booking-view/<int:id>',views.booking_view),
    path('super/booking-edit/<int:id>',views.booking_edit),
    path('super/booking-update/<int:id>',views.booking_update),

# Rate Type 
    path('super/discount-type', views.discount_type),
    path('super/discount-type-add', views.discount_type_add),
    path('super/discount-type-insert', views.discount_type_insert),
    path('super/discount-type-edit/<int:id>', views.discount_type_edit), 
    path('super/discount-type-update/<int:id>', views.discount_type_update),  
    path('super/discount-type-delete/<int:id>', views.discount_type_destroy),

# Discount
    path('super/discounts', views.discount),
    path('super/discount-add', views.discount_add),
    path('super/discount-insert', views.discount_insert),
    path('super/discount-edit/<int:id>', views.discount_edit), 
    path('super/discount-update/<int:id>', views.discount_update),  
    path('super/discount-delete/<int:id>', views.discount_destroy), 

# Currency
    path('super/currency', views.currency),
    path('super/currency-add', views.currency_add),
    path('super/currency-insert', views.currency_insert),
    path('super/currency-edit/<int:id>', views.currency_edit), 
    path('super/currency-update/<int:id>', views.currency_update),  
    path('super/currency-delete/<int:id>', views.currency_destroy),

# Invoice   
    path('super/invoice/', views.InvoiceListView.as_view(), name="invoice-list"),
    path('super/invoice-create/', views.createInvoice, name="invoice-create"),
    path('super/invoice-detail/<id>', views.view_PDF, name='invoice-detail'),
    path('super/invoice-download/<id>', views.generate_PDF, name='invoice-download'),
    path('super/company-add',views.company_add), 
    path('super/company-insert',views.company_insert), 
    path('super/company',views.company),  
    path('super/company-edit/<int:id>', views.company_edit),  
    path('super/company-update/<int:id>', views.company_update),  
    path('super/company-delete/<int:id>', views.company_destroy),
      
# # Rental Gallery
#     path('super/rentals-gallery-insert/<int:id>',views.rentals_gallery_insert),
#     path('super/rentals-gallery/<int:id>',views.rentals_gallery),
#     path('super/rentals-gallery-add',views.rentals_gallery_add),
     
# Attributes
    path('super/attributes-insert',views.attributes_insert),  
    path('super/attributes-add',views.attributes_add), 
    path('super/attributes',views.attributes),  
    path('super/attributes-edit/<int:id>', views.attributes_edit),  
    path('super/attributes-update/<int:id>', views.attributes_update),  
    path('super/attributes-delete/<int:id>', views.attributes_destroy),
    path('super/calendar', views.calendar),
    path('super/reports', views.reports),

    path('super/change-password', views.change_password, name='change_password'),

# Partner category  
    path('super/partner-category-add',views.category_add),  
    path('super/partner-category-insert',views.category_insert), 
    path('super/partners-category',views.category),  
    path('super/partner-category-edit/<int:id>', views.category_edit),  
    path('super/partner-category-update/<int:id>', views.category_update),  
    path('super/partner-category-delete/<int:id>', views.category_destroy),

# Partner 
    path('super/partner-add',views.partner_add),  
    path('super/partner-insert',views.partner_insert), 
    path('super/partner',views.partner),  
    path('super/partner-edit/<int:id>', views.partner_edit),  
    path('super/partner-update/<int:id>', views.partner_update),  
    path('super/partner-delete/<int:id>', views.partner_destroy),
# Subscription
    path('super/subscription', views.subscription),
    path('super/subscription-add', views.subscription_add),
    path('super/subscription-insert', views.subscription_insert),
    path('super/subscription-edit/<int:id>', views.subscription_edit),
    path('super/subscription-update/<int:id>', views.subscription_update),
    path('super/subscription-delete/<int:id>', views.subscription_destroy),
# Country
    path('super/country', views.country),
    path('super/country-add', views.country_add),
    path('super/country-insert', views.country_insert),
    path('super/country-edit/<int:id>', views.country_edit),
    path('super/country-update/<int:id>', views.country_update),
    path('super/country-delete/<int:id>', views.country_destroy),
# Property Role
    path('super/property-role', views.property_role),
    path('super/property-role-add', views.property_role_add),
    path('super/property-role-insert', views.property_role_insert),
    path('super/property-role-edit/<int:id>', views.property_role_edit),
    path('super/property-role-update/<int:id>', views.property_role_update),
    path('super/property-role-delete/<int:id>', views.property_role_destroy),
# Room-Type 
    path('super/room-type', views.room_type),
    path('super/room-type-add', views.room_type_add),
    path('super/room-type-insert', views.room_type_insert),
    path('super/room-type-edit/<int:id>', views.room_type_edit),
    path('super/room-type-update/<int:id>', views.room_type_update),
    path('super/room-type-delete/<int:id>', views.room_type_destroy),
# Rooms 
    path('super/rooms', views.rooms),
    path('super/room-add', views.room_add),
    path('super/room-insert', views.room_insert),
    path('super/room-edit/<int:id>', views.room_edit),
    path('super/room-update/<int:id>', views.room_update),
    path('super/room-delete/<int:id>', views.room_destroy),
# Beds 
    path('super/beds', views.beds),
    path('super/bed-add', views.bed_add),
    path('super/bed-insert', views.bed_insert),
    path('super/bed-edit/<int:id>', views.bed_edit),
    path('super/bed-update/<int:id>', views.bed_update),
    path('super/bed-delete/<int:id>', views.bed_destroy),

    path('super/other-rooms', views.other_rooms),
    path('super/other-room-add', views.other_room_add),
    path('super/other-room-insert', views.other_room_insert),
    path('super/other-room-edit/<int:id>', views.other_rooms_edit),
    path('super/other-room-update/<int:id>', views.other_room_update),
    path('super/other-room-delete/<int:id>', views.other_room_destroy), 

    path('super/rental-basic/<int:id>', views.rental_basic),
    path('super/rental-basic-update/<int:id>', views.rental_basic_update),
    path('super/rental-location/<int:id>', views.rental_location),
    path('super/rental-location-update/<int:id>', views.rental_location_update),
    path('super/rental-rooms/<int:id>', views.rental_rooms),
    path('super/other-rooms-insert/<int:id>', views.rental_other_rooms_insert),
    path('super/rental-amenities/<int:id>', views.rental_amenities),
    path('super/rental-amenities-update/<int:id>', views.rental_amenities_update),
    path('super/basic-rates/<int:id>', views.rental_basic_rates),
    path('super/basic-rates-update/<int:id>', views.rental_basic_rates_update),
    path('super/seasonal-rates-update/<int:id>', views.rental_seasonal_rates_update),
    path('super/seasonal-rates-insert/<int:id>', views.rental_seasonal_rates_insert),
    path('super/seasonal-rates/<int:id>', views.rental_seasonal_rates),
    path('super/seasonal-rates-delete/<int:id>', views.rental_seasonal_destroy),
    path('super/rental-discounts/<int:id>', views.rental_discount),
    path('super/long-stay-discounts/<int:id>', views.long_stay_discount_update),
    path('super/early-bird-discounts/<int:id>', views.early_bird_discount_update),
    path('super/rental-additional-info/<int:id>', views.rental_additional_info),
    path('super/cleaning-update/<int:id>', views.rental_cleaning_update),
    path('super/deposit-update/<int:id>', views.rental_deposit_update),
    path('super/tax-insert/<int:id>', views.rental_tax_insert),
    path('super/tax-update/<int:id>', views.rental_tax_update),
    path('super/tax-delete/<int:id>', views.rental_tax_destroy),
    path('super/extra-services-insert/<int:id>', views.rental_extra_services_insert),
    path('super/custom-services-insert/<int:id>', views.rental_custom_services_insert),
    path('super/rental-house-rules/<int:id>', views.rental_house_rules),
    path('super/rental-house-rules-update/<int:id>', views.rental_house_rules_update),
    path('super/rental-policy/<int:id>', views.rental_policy),
    path('super/rental-policy-update/<int:id>', views.rental_policy_update),
    path('super/rental-instructions/<int:id>', views.rental_instruction),
    path('super/rental-instruction-update/<int:id>', views.rental_instruction_update),
    path('super/select-channels/<int:id>', views.rental_select_channels),
    path('super/channel-insert', views.channel_insert),
    path('rentals-gallery-insert/<int:id>',views.rentals_gallery_insert),
    path('super/rental-photo/<int:id>',views.rentals_gallery),
    path('delete-gallery/<int:id>',views.gallery_destroy),

    # Services 
    path('super/services', views.services),
    path('super/services-add', views.services_add),
    path('super/services-insert', views.services_insert),
    path('super/services-edit/<int:id>', views.services_edit),
    path('super/services-update/<int:id>', views.services_update),
    path('super/services-delete/<int:id>', views.services_destroy),

    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
    