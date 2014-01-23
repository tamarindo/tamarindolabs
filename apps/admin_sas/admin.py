from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(DniType)