from rest_framework.serializers import ModelSerializer
from .models import car_model, engine_model, employee, department


class car_serializer(ModelSerializer):
    class Meta:
        model = engine_model
        fields = '__all__'
        depth = 1


class engine_serializer(ModelSerializer):
    class Meta:
        model = car_model
        fields = '__all__'


class department_serialzer(ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class employee_serializer(ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


