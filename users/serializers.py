from rest_framework_json_api import serializers
from rentals.models import Bookings, Rental, RentalBasic, RentalsGallery, RentalLocation, RentalOtherRooms, RentalAmenities, BasicRates, SeasonalRates, RentalDeposit, LongStayDiscount, EarlyBirdDiscount, RentalCleaning, RentalTax, ExtraServices, CustomServices, HouseRules, RentalPolicy, RentalInstruction

class RentalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'rental_name','rental_short_description','rental_description','cover_image')

class RentalBasicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalBasic
        fields = ('rental_type','rental_basis','floorspace','floorspace_units','grounds','grounds_units','floors_building','entrance','rental_licence','rental_id','user_id')

class RentalGallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalsGallery
        fields = ('image', 'user_id','rental_id')

class RentalLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalLocation
        fields = ('country', 'address', 'apartment', 'city', 'state', 'postal', 'user_id','rental_id')

class RentalOtherRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalOtherRooms
        fields = ('other_rooms', 'user_id','rental_id')

class RentalAmenitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalAmenities
        fields = ('amenities', 'user_id','rental_id')

class RentalBasicRatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasicRates
        fields = ('currency', 'basic_night','weekend_night','guest_number','minimum_stay','maximum_stay', 'checkin_days', 'checkout_days', 'user_id','rental_id')

class RentalSeasonalRatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonalRates
        fields = ('season_name', 'start_date','end_date','basic_night','weekend_night', 'minimum_stay', 'maximum_stay', 'checkin_days', 'checkout_days', 'user_id','rental_id')

class RentalDepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalDeposit
        fields = ('security_deposit', 'amount', 'user_id','rental_id')

class RentalLongStayDiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LongStayDiscount
        fields = ('seven_nights', 'fourteen_nights', 'twenty_one_nights', 'twenty_eight_nights','user_id','rental_id')

class RentalEarlyBirdDiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EarlyBirdDiscount
        fields = ('booking_less', 'booking_less_discount', 'booking_more', 'booking_more_discount','user_id','rental_id')    

class RentalCleaningSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalCleaning
        fields = ('cleaning_available', 'cleaning_basis', 'price', 'user_id','rental_id')    

class RentalTaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalTax
        fields = ('tax_type', 'fee_basis', 'percentage', 'amountin', 'user_id','rental_id') 

class RentalExtraServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraServices
        fields = ('service_name', 'service_provided', 'fee_basis', 'service_price', 'earliest_guest_order', 'latest_guest_order', 'guest_cancel_order', 'extra_message','user_id','rental_id') 

class RentalCustomServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomServices
        fields = ('custom_service_name', 'custom_service_provided', 'custom_fee_basis', 'custom_service_price', 'custom_earliest_guest_order', 'custom_latest_guest_order', 'custom_guest_cancel_order', 'custom_extra_message','user_id','rental_id') 

class RentalHouseRulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HouseRules
        fields = ('for_kid', 'wheelchair_access', 'parties_allowed', 'smoking_allowed', 'pets', 'house_rules', 'user_id','rental_id') 

class RentalPolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalPolicy
        fields = ('name', 'description', 'user_id','rental_id') 

class RentalInstructionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalInstruction
        fields = ('checkin_instruction', 'checkout_instruction', 'checkin_contact', 'key_collection', 'telephone_country', 'telephone_number', 'instructions', 'attach_instruction', 'checkin_from', 'checkout_until', 'airport_instruction', 'property_directions','dialing_code', 'user_id','rental_id') 

class BookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookings
        fields = ('rental','check_in','check_out','user_id')