from django.contrib import admin
from .models import *


admin.site.register(Feedback)

admin.site.register(People)

admin.site.register(Telegramm_Reviews)
admin.site.register(Discord_Reviews)

admin.site.register(Telegramm_Bots)
admin.site.register(Discord_Bots)