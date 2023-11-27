from rest_framework import serializers

from cars.models import Car, ParkingLot


class ParkingLotSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = ParkingLot
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    year = serializers.DateTimeField()
    is_parked = serializers.BooleanField(default=False)  # type: ignore

    class Meta:
        model = Car
        fields = '__all__'
