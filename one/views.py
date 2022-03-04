from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import car_model, engine_model, employee, department
from .seralizers import engine_serializer, car_serializer, employee_serializer

from rest_framework.response import Response


class func1(ModelViewSet):
    queryset = car_model.objects.all()
    serializer_class = car_serializer

    def create(self, request):
        model__ = engine_model.objects.create(
            cc=request.data["_new"]["cc"],
            color=request.data["_new"]["color"]
        )
        model__.save()
        model_ = car_model.objects.create(
            name=request.data["name"],
            model_no=request.data["model_no"],
            _new=model__,
        )
        model_.save()
        response = {
            'message': 'created'
        }
        return Response(response)


class second_view(ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employee_serializer

    def create_2(self, request):
        model__ = department.objects.create(
            name=request.data["_info"]["name"],
            location=request.data["_info"]["location"],
        )
        model__.save()
        model_ = employee.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            _info=model__
        )
        model_.save()
        response = {
            'message': 'created'
        }
        return Response(response)
