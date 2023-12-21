from django.contrib import admin
from .models import Construction, Order, SubwayStation, ConstructionThreeDImage
# Register your models here.


admin.site.register(Construction)
admin.site.register(Order)
admin.site.register(SubwayStation)
admin.site.register(ConstructionThreeDImage)