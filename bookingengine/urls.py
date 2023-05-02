from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static

app_name = 'bookingengine' 
urlpatterns = [

# index
    path('dashboard',views.index),
    path('',views.signin),
    path('signin',views.signin),
    path('signup',views.signup),
    path('signout',views.signout),
  
    
# Rental Type  
    path('room-add',views.room_add),  
    path('room-insert',views.room_insert), 
    path('rooms',views.rooms),  
    path('room-edit/<int:id>', views.room_edit),  
    path('room-update/<int:id>', views.room_update),  
    path('room-delete/<int:id>', views.room_destroy),

#Amenities
    path('amenities-insert',views.amenities_insert),
    path('amenities',views.amenities),
    path('amenities-add',views.amenities_add),
    path('amenities-edit/<int:id>',views.amenities_edit),
    path('amenities-update/<int:id>',views.amenities_update),
    path('amenities-delete/<int:id>',views.amenities_destroy),

#Categories
    path('category-insert',views.category_insert),
    path('categories',views.category),
    path('category-add',views.category_add),
    path('category-edit/<int:id>',views.category_edit),
    path('category-update/<int:id>',views.category_update),
    path('category-delete/<int:id>',views.category_destroy),

#Tags
    path('tag-insert',views.tag_insert),
    path('tags',views.tag),
    path('tag-add',views.tag_add),
    path('tag-edit/<int:id>',views.tag_edit),
    path('tag-update/<int:id>',views.tag_update),
    path('tag-delete/<int:id>',views.tag_destroy),    

#Seasons
    path('season-insert',views.season_insert),
    path('seasons',views.seasons),
    path('season-add',views.season_add),
    path('season-edit/<int:id>',views.season_edit),
    path('season-update/<int:id>',views.season_update),
    path('season-delete/<int:id>',views.season_destroy),

#Rates
    path('rate-insert',views.rate_insert),
    path('rates',views.rates),
    path('rate-add',views.rate_add),
    path('rate-edit/<int:id>',views.rate_edit),
    path('rate-update/<int:id>',views.rate_update),
    path('rate-delete/<int:id>',views.rate_destroy),

#Services
    path('service-insert',views.service_insert),
    path('services',views.services),
    path('service-add',views.service_add),
    path('service-edit/<int:id>',views.service_edit),
    path('service-update/<int:id>',views.service_update),
    path('service-delete/<int:id>',views.service_destroy),

#Taxes
    path('tax-insert',views.tax_insert),
    path('tax-add',views.tax_add),     
    path('tax',views.tax),    
    path('tax-edit/<int:id>',views.tax_edit),
    path('tax-update/<int:id>',views.tax_update),
    path('tax-delete/<int:id>',views.tax_destroy),

#Profile
    path('profile',views.profile),
    path('profile-update/<int:id>',views.profile_update),

#Gallery
    path('rooms-gallery/<int:id>',views.rooms_gallery),
    path('rooms-gallery-insert/<int:id>',views.rooms_gallery_insert),
    path('rooms-gallery-delete/<int:id>',views.gallery_destroy),

    path('overview-search',views.overview),
    path('overview',views.overview_all),
    path('overview-grid',views.overview_grid),
    path('room-details/<int:id>',views.room_details),
    path('preview/<int:id>',views.preview),
    path('book-room/book', views.book_room,name="bookroom"),
    path('book-room', views.book_room_page,name="bookroompage"),
    path('social-media', views.social_media_view),
    path('contact-info', views.contact_info_view),
    path('color-palette', views.color_palette),
    path('term-condition', views.term_condition),
    path('get_session_data', views.get_session_data),
    path('booking-information', views.booking_information),
    

    
#Coupons
    path('coupon-insert',views.coupon_insert),
    path('coupon-add',views.coupon_add),    
    path('coupons',views.coupons),    
    path('coupon-edit/<int:id>',views.coupon_edit),
    path('coupon-update/<int:id>',views.coupon_update),
    path('coupon-delete/<int:id>',views.coupon_destroy),     

#Widgets
    path('widget-insert',views.widget_insert),
    path('widget-add',views.widget_add),    
    path('widgets',views.widgets),    
    path('widget-edit/<int:id>',views.widget_edit),
    path('widget-update/<int:id>',views.widget_update),
    path('widget-delete/<int:id>',views.widget_destroy),      

#ExtraService
    path('extra-service-insert',views.extra_service_insert),
    path('extra-service-add',views.extra_service_add),    
    path('extra-services',views.extra_services),    
    path('extra-service-edit/<int:id>',views.extra_service_edit),
    path('extra-service-update/<int:id>',views.extra_service_update),
    path('extra-service-delete/<int:id>',views.extra_service_destroy),      


]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   