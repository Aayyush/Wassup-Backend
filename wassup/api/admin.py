from django.contrib import admin
from .models import Profile, Criteria, Event 

# Register your models here.
admin.site.register(Profile)
admin.site.register(Criteria)
admin.site.register(Event)