import uuid

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from cars.models import Car, ParkingLot
from cars.serializer import CarSerializer, ParkingLotSerializer


class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'parking_lot_id': openapi.Schema(type=openapi.TYPE_STRING, description="Parking lot ID")
        }),
        operation_description="Park a car",
        responses={
            status.HTTP_200_OK: "Car parked",
            status.HTTP_400_BAD_REQUEST: "Car is already parked",
            status.HTTP_404_NOT_FOUND: "Parking lot not found",
            status.HTTP_422_UNPROCESSABLE_ENTITY: "Parking lot ID is required and must be a valid UUID",
        }
    )
    @action(detail=True, methods=['post'])
    def park(self, request: Request, pk: str):
        car: Car = self.get_object()

        if car.is_parked:
            return Response({'message': 'Car is already parked'}, status=status.HTTP_400_BAD_REQUEST)

        parking_lot_id = request.data.get("parking_lot_id")
        parking_lot_uuid = uuid.UUID(parking_lot_id)
        if not parking_lot_id or not parking_lot_uuid:
            return Response({'message': 'Parking lot ID is required'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            parking_lot: ParkingLot = ParkingLot.objects.get(id=parking_lot_id)

        except ParkingLot.DoesNotExist:
            return Response({'message': 'Parking lot not found'}, status=status.HTTP_404_NOT_FOUND)

        car.is_parked = True
        car.parked_in = parking_lot

        car.save()        

        return Response({'message': 'Parked'}, status=status.HTTP_200_OK)
