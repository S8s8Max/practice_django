from django.contrib import admin
from .models import Message, Good, Group, Friend

# Register your models here.
admin.site.register(Message)
admin.site.register(Good)
admin.site.register(Group)
admin.site.register(Friend)
