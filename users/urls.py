from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static

app_name = 'users'  
urlpatterns = [


    path('test/', views.test_view, name='test_view'),

# index
    path('dashboard',views.index),
    path('customers',views.customers),
    path('',views.signin),
    path('signup',views.signup),
    path('logout',views.signout),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset-password',views.resetpassword),
    
# Rental Type  
    path('rental-type-add',views.rental_type_add),  
    path('rental-type-insert',views.rental_type_insert), 
    path('rental-type',views.rental_type),  
    path('rental-type-edit/<int:id>', views.rental_type_edit),  
    path('rental-type-update/<int:id>', views.rental_type_update),  
    path('rental-type-delete/<int:id>', views.rental_type_destroy),
    
# Rentals
    path('rentals/overview',views.rental_add),
    path('rental-insert',views.rental_insert),
    path('rentals',views.rentals),    
    path('rentals/overview/<int:id>', views.rental_edit), 
    path('rentals/preview/<int:id>', views.rental_preview),   
    path('rental-update/<int:id>', views.rental_update),  
    path('rental-delete/<int:id>', views.rental_destroy),
    path('rentals/basic/<int:id>', views.rental_basic),
    path('rentals/rental-basic-update/<int:id>', views.rental_basic_update),
    path('rentals/location/<int:id>', views.rental_location),
    path('rentals/rental-location-update/<int:id>', views.rental_location_update),
    path('rentals/rooms/<int:id>', views.rental_rooms),
    path('rentals/other-rooms-update/<int:id>', views.rental_other_room_update),
    path('rentals/amenities/<int:id>', views.rental_amenities),
    path('rentals/rental-amenities-update/<int:id>', views.rental_amenities_update),
    path('rentals/basic-rates/<int:id>', views.rental_basic_rates),
    path('rentals/basic-rates-update/<int:id>', views.rental_basic_rates_update),
    path('rentals/seasonal-rates-update/<int:id>', views.rental_seasonal_rates_update),
    path('rentals/seasonal-rates-insert/<int:id>', views.rental_seasonal_rates_insert),
    path('rentals/seasonal-rates/<int:id>', views.rental_seasonal_rates),
    path('rentals/seasonal-rates-delete/<int:id>', views.rental_seasonal_destroy),
    path('rentals/discounts/<int:id>', views.rental_discount),
    path('rentals/long-stay-discounts/<int:id>', views.long_stay_discount_update),
    path('rentals/early-bird-discounts/<int:id>', views.early_bird_discount_update),
    path('rentals/additional-info/<int:id>', views.rental_additional_info),
    path('get_data_for_id/', views.get_data_for_id),
    path('get_data_for_extra/', views.get_data_for_extra),
    path('get_data_for_tax/', views.get_data_for_tax),
    path('rentals/cleaning-update/<int:id>', views.rental_cleaning_update),
    path('rentals/deposit-update/<int:id>', views.rental_deposit_update),
    path('rentals/tax-insert/<int:id>', views.rental_tax_insert),
    path('rentals/tax-update/<int:id>', views.rental_tax_update),
    path('rentals/tax-delete/<int:id>', views.rental_tax_destroy),
    path('rentals/extra-services-insert/<int:id>', views.rental_extra_services_insert),
    path('rentals/extra-services-update/<int:id>', views.rental_extra_services_update),
    path('rentals/extra-services-delete/<int:id>', views.rental_extra_services_destroy),
    path('rentals/custom-services-insert/<int:id>', views.rental_custom_services_insert),
    path('rentals/custom-services-update/<int:id>', views.rental_custom_services_update),
    path('rentals/custom-services-delete/<int:id>', views.rental_custom_services_destroy),
    path('rentals/house-rules/<int:id>', views.rental_house_rules),
    path('rentals/house-rules-update/<int:id>', views.rental_house_rules_update),
    path('rentals/policy/<int:id>', views.rental_policy),
    path('rentals/policy-update/<int:id>', views.rental_policy_update),
    path('rentals/instructions/<int:id>', views.rental_instruction),
    path('rentals/instruction-update/<int:id>', views.rental_instruction_update),
    path('rentals/select-channels/<int:id>', views.rental_select_channels),
    path('rentals/channel-update/<int:id>', views.rental_channel_update),


# Channels  
  
    # path('channel-insert/<int:id>',views.channel_insert), 
    path('channels',views.channels),  
    path('channel-edit/<int:id>', views.channel_edit),  
    path('channel-update/<int:id>', views.channel_update),  
    path('channel-delete/<int:id>', views.channel_destroy), 
    
# Policy
    path('policy', views.policy),
    path('policy-add', views.policy_add),
    path('policy-insert', views.policy_insert),
    path('policy-edit/<int:id>', views.policy_edit), 
    path('policy-update/<int:id>', views.policy_update),
    path('policy-delete/<int:id>', views.policy_destroy), 
    
# Bookings
    path('bookings',views.booking),
    path('booking-view/<int:id>',views.booking_view),
    path('booking-edit/<int:id>',views.booking_edit),
    path('booking-update/<int:id>',views.booking_update),
    path('reservation/<int:id>',views.booking_list),
    
# Invoice   
    path('invoice/', views.InvoiceListView.as_view(), name="invoice-list"),
    path('invoice-create/', views.createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', views.view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', views.generate_PDF, name='invoice-download'),
    path('company-add',views.company_add), 
    path('company-insert',views.company_insert), 
    path('company',views.company),  
    path('company-edit/<int:id>', views.company_edit),  
    path('company-update/<int:id>', views.company_update),  
    path('company-delete/<int:id>', views.company_destroy),

# Discount
    path('discounts', views.discount),
    path('discount-add', views.discount_add),
    path('discount-insert', views.discount_insert),
    path('discount-edit/<int:id>', views.discount_edit), 
    path('discount-update/<int:id>', views.discount_update),  
    path('discount-delete/<int:id>', views.discount_destroy), 

# Discount Type 
    path('discount-type', views.discount_type),
    path('discount-type-add', views.discount_type_add),
    path('discount-type-insert', views.discount_type_insert),
    path('discount-type-edit/<int:id>', views.discount_type_edit), 
    path('discount-type-update/<int:id>', views.discount_type_update),  
    path('discount-type-delete/<int:id>', views.discount_type_destroy),

# Currency
    path('currency', views.currency),
    path('currency-add', views.currency_add),
    path('currency-insert', views.currency_insert),
    path('currency-edit/<int:id>', views.currency_edit), 
    path('currency-update/<int:id>', views.currency_update),  
    path('currency-delete/<int:id>', views.currency_destroy), 

# Rate Type    
    path('rate-type', views.rate_type),
    path('rate-type-add', views.rate_type_add),
    path('rate-type-insert', views.rate_type_insert),
    path('rate-type-edit/<int:id>', views.rate_type_edit), 
    path('rate-type-update/<int:id>', views.rate_type_update),  
    path('rate-type-delete/<int:id>', views.rate_type_destroy), 

# Rate 
    path('rate', views.rate),
    path('rate-add', views.rate_add),
    path('rate-insert', views.rate_insert),
    path('rate-edit/<int:id>', views.rate_edit), 
    path('rate-update/<int:id>', views.rate_update),  
    path('rate-delete/<int:id>', views.rate_destroy), 
    
# Tax
    path('tax-add',views.tax_add), 
    path('tax-insert',views.tax_insert), 
    path('tax',views.tax),  
    path('tax-edit/<int:id>', views.tax_edit),  
    path('tax-update/<int:id>', views.tax_update),  
    path('tax-delete/<int:id>', views.tax_destroy), 
    
# Tax Type
    path('tax-type', views.tax_type),
    path('tax-type-add', views.tax_type_add),
    path('tax-type-insert', views.tax_type_insert),
    path('tax-type-edit/<int:id>', views.tax_type_edit), 
    path('tax-type-update/<int:id>', views.tax_type_update),  
    path('tax-type-delete/<int:id>', views.tax_type_destroy),
    
# Amenities
    path('amenities-insert',views.amenities_insert),  
    path('amenities-add',views.amenities_add), 
    path('amenities',views.amenities),  
    path('amenities-edit/<int:id>', views.amenities_edit),  
    path('amenities-update/<int:id>', views.amenities_update),  
    path('amenities-delete/<int:id>', views.amenities_destroy),
    
# Activity
    path('activity',views.activity),  
    path('activity-add',views.activity_add),
    path('activity-insert',views.activity_insert),  
    path('activity-edit/<int:id>', views.activity_edit),  
    path('activity-update/<int:id>', views.activity_update),  
    path('activity-delete/<int:id>', views.activity_destroy),
    
# Calendar
    # path('calendar',views.calendar),
    # path('calendar/<int:id>',views.calendar),
    path("calendar", views.CalendarViewNew.as_view(), name="calendar"),
    path("calendar-delete/<int:id>", views.cal_destroy),
    
# Rental Gallery
    # path('rentals-gallery-insert/<int:id>',views.rentals_gallery_insert),
    path('rentals-gallery-insert/<int:id>',views.rentals_gallery_insert),
    path('rentals/photo/<int:id>',views.rentals_gallery),
    path('delete-gallery/<int:id>',views.gallery_destroy),


# Attributes
    path('attributes',views.attributes),
    path('attributes-add',views.attributes_add),
    path('attributes-insert',views.attributes_insert),
    path('attributes-edit/<int:id>', views.attributes_edit),  
    path('attributes-update/<int:id>', views.attributes_update),  
    path('attributes-delete/<int:id>', views.attributes_destroy),

# Customers
    path('customers',views.customers),

# Reports
    path('reports',views.reports),
    path('profile',views.profile),
    path('profile-update/<int:id>',views.profile_update),
    path('subscription',views.subscription),
    path('go-back',views.error_back),
    path('sort',views.sort),
    path('subscription-insert/<int:id>',views.subscription_insert, name="subscription"), 

    path('update-rooms/<int:id>',views.update_rooms),
    path('insert-beds/<int:id>',views.insert_beds),
    path('api',views.my_view),
    path('analytics',views.chart)




]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   