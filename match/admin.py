from django.contrib import admin
from match.models import Match

# Register your models here.
#class MatchAdmin(admin.ModelAdmin):
admin.site.register(Match)    
