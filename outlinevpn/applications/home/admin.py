from django.contrib import admin

from .models import Producto,Principal,FAQ

# Register your models here.
admin.site.register(Principal)
admin.site.register(FAQ)
admin.site.register(Producto)
