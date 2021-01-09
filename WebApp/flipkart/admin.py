from django.contrib import admin
from .models import Feedback, ProductInformation, Cart

# Register your models here.

admin.site.register(Feedback)
admin.site.register(ProductInformation)
admin.site.register(Cart)
