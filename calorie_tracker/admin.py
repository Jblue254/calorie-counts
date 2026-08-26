from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "food",
        "meal",
        "day",
        "calories",
        "created_at"
    )

    search_fields = (
        "food",
        "meal"
    )

    list_filter = (
        "day",
        "meal"
    )