from django.contrib import admin
from django.contrib import admin
from rentals.models import Activity, Amenities, Bookings, Category, Channel, ChannelManagement, CompanyProfile, Country, Invoice, InvoiceItem, Partner, Rate, Ratetype, Rental, RentalInstruction, RentalOtherRooms, RentalsGallery, Rentaltype, Subscription, Tax, Taxtype, UserProfile,Event

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Channel)
admin.site.register(Amenities)
admin.site.register(Activity)
admin.site.register(Rentaltype)
admin.site.register(Taxtype)
admin.site.register(Tax)
admin.site.register(Ratetype)
admin.site.register(Rate)
admin.site.register(Bookings)
admin.site.register(InvoiceItem)
admin.site.register(Invoice)
admin.site.register(CompanyProfile)
admin.site.register(Rental)
admin.site.register(RentalsGallery)
admin.site.register(RentalInstruction)
admin.site.register(ChannelManagement)
admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Country)
admin.site.register(RentalOtherRooms)






