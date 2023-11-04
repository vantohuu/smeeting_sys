# Generated by Django 4.2.1 on 2023-05-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gb', '0002_gb_model'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GB_Model',
        ),
        migrations.RemoveField(
            model_name='gb',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='gb',
            name='description',
        ),
        migrations.RemoveField(
            model_name='gb',
            name='title',
        ),
        migrations.AddField(
            model_name='gb',
            name='arrival_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='arrival_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='arrival_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='avg_price_per_room',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='lead_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='market_segment_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_adults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_previous_bookings_not_canceled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_previous_cancellations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_special_requests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_week_nights',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='no_of_weekend_nights',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='repeated_guest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='required_car_parking_space',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='room_type_reserved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gb',
            name='type_of_meal_plan',
            field=models.IntegerField(default=0),
        ),
    ]
