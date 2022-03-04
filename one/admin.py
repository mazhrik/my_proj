from django.contrib import admin
from .models import car_model, engine_model, department, employee

# Register your models here.
admin.site.register(car_model)
admin.site.register(engine_model)
admin.site.register(department)
admin.site.register(employee)
