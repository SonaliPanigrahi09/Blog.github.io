from django.contrib import admin
from home.models import Contact

# Register your models here.
# registering models helps to show up in admin pannel
#ALL models created must be registerd here.

admin.site.register(Contact)
