from rest_framework import serializers
from .models import GB

class GBSerializer(serializers.ModelSerializer):
    class Meta:
        model = GB
#        fields = ('id', 'title', 'description', 'completed')
        fields = ('no_of_adults','no_of_children','no_of_weekend_nights','no_of_week_nights','type_of_meal_plan','required_car_parking_space','room_type_reserved','lead_time','arrival_year','arrival_month','arrival_date','market_segment_type','repeated_guest','no_of_previous_cancellations','no_of_previous_bookings_not_canceled','avg_price_per_room','no_of_special_requests')


#class GBMDSerializer(serializers.ModelSerializer):
 #   class Meta:
 #       model = GB_Model
  #      fields = ('id', 'no_of_adults','no_of_children','no_of_weekend_nights','no_of_week_nights','type_of_meal_plan','required_car_parking_space','room_type_reserved','lead_time','arrival_year','arrival_month','arrival_date','market_segment_type','repeated_guest','no_of_previous_cancellations','no_of_previous_bookings_not_canceled','avg_price_per_room','no_of_special_requests')

