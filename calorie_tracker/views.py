from django.shortcuts import render
from .models import FoodItem

def home(request):
    foods = FoodItem.objects.all()
    total_calories = sum(food.calories for food in foods)

    context = {
        "foods": foods,
        "total_calories": total_calories,
    }

    return render(request, "calorie_tracker/index.html", context)