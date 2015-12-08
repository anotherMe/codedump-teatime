from django.contrib import admin

# Register your models here.

from .models import Sample
from .models import Shop
from .models import Pin

admin.site.register(Sample)
admin.site.register(Shop)
admin.site.register(Pin)
