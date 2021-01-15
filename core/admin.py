from django.contrib import admin
from .models import Contact

from .views import *
admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Contact)

