from django.contrib import admin
from .models import CustomUser,Transaction,Balance




admin.site.register(CustomUser)
admin.site.register(Transaction)
admin.site.register(Balance)


