from django.contrib import admin
from cart.models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(Score, ScoreAdmin)
