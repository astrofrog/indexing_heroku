from django.contrib import admin
from main.models import Quantity, QuantityDefinition, User, Object

admin.site.register(Quantity)
admin.site.register(QuantityDefinition)
admin.site.register(Object)
admin.site.register(User)