from django.contrib import admin
from .models import HomePage


@admin.register(HomePage)
class Home(admin.ModelAdmin):
    """
    Admin access to models.py to update mission statement
    and how you can help.
    """
    list_display = ('heading', 'statement', 'date')
