"""ezbzrental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include  
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
#API URL Routes start

router.register('api/rentals', views.RentalViewSet)
router.register('api/rental-basic', views.RentalBasicViewSet)
router.register('api/rental-gallery', views.RentalsGalleryViewSet)
router.register('api/rental-location', views.RentalsLocationViewSet)
router.register('api/rental-other-room', views.RentalsOtherRoomViewSet)
router.register('api/rental-amenities', views.RentalAmenitiesViewSet)
router.register('api/rental-basic-rates', views.RentalBasicRatesViewSet)
router.register('api/rental-seasonal-rates', views.RentalSeasonalRatesViewSet)
router.register('api/rental-deposit', views.RentalDepositViewSet)
router.register('api/rental-longstay-discount', views.RentalLongStayDiscountViewSet)
router.register('api/rental-earlybird-discount', views.RentalEarlyBirdDiscountViewSet)
router.register('api/rental-cleaning', views.RentalCleaningViewSet)
router.register('api/rental-tax', views.RentalTaxViewSet)
router.register('api/rental-extra-services', views.RentalExtraServicesViewSet)
router.register('api/rental-custom-services', views.RentalCustomServicesViewSet)
router.register('api/rental-house-rules', views.RentalHouseRulesViewSet)
router.register('api/rental-policy', views.RentalPolicyViewSet)
router.register('api/rental-instruction', views.RentalInstructionViewSet)
router.register('api/bookings', views.BookingsViewSet)


#API URL Routes End

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('rentals.urls')),
    path('',include('agent.urls')),
    path('',include('users.urls')),
    path('booking-engine/',include('bookingengine.urls')),
    path('', include(router.urls)),
    
]
handler404 = 'users.views.error_404_view'
