from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry, Re_Entry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Re_Entry)
